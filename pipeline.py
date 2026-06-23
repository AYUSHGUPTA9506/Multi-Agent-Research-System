from agents import build_reader_agent, build_search_agent, writer_chain, critic_chain

def run_research_pipeline(topic:str)-> dict:
    
    state={}
    
    #step1
    #search agent working
    print("\n ="*50)
    print("step1- search agent is working...")
    print("="*50)
    
    
    #search agent will provide internal loop and then provide result
    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages":[("user",f"Find recent, reliable and detailed information about: {topic}")]
        
    })#a different type of input and output in react agent vs create agent
     
    state["search_results"]=search_result['messages'][-1].content
    
    print("\n search result ",state['search_results'])
    
    
    #step2
    #reader_agent working
    print("\n ="*50)
    print("step 2 - Reader agent is scraping top resources ...")
    print("="*50)
    
    #this reader agent will scrap the contents from the strings 
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
        
    })
    state['scraped_content'] = reader_result['messages'][-1].content
    
    print("\nscrapped content\n",state['scraped_content'])
    
    #now we have all the infos from search to scrapping and then we will chai them with StrOutParser
    #1st chain is the writer chain which we need and the next chain will be the critic chain which will evaluate our results
    
    
    #step3-writer chain
    
    print("\n"+" ="*50)
    print("step 3 - Writer is drafting the report ...")
    print("="*50)
    
    research_combined = (
        f"SEARCH RESULTS : \n{state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT : \n{state['scraped_content']}"
    )
    
    state['report'] = writer_chain.invoke({
        "topic" : topic,
        "research" : research_combined
    })
    
    print("\n Final Report \n",state['report'])
    
    #step 4 critic report
    
    print("\n"+" ="*50)
    print("step 4 - critic is reviewing the report ")
    print("="*50)
    state["feedback"]=critic_chain.invoke({
        "report":state['report']
    })
    
    print("\n critic report \n", state['feedback'])
    
    return state
    
if __name__ == "__main__":#whenver i have to call pipeline.py
    topic=input("\n Enter a research topic :")
    run_research_pipeline(topic)
 
    