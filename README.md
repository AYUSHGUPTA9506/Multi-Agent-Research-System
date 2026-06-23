# 🤖 Multi-Agent Research AI System

An advanced AI-powered research assistant built using a **Multi-Agent architecture**. Multiple specialized AI agents collaborate together to perform deep research, gather information, analyze data, and deliver comprehensive results — all through natural language.

---

## 🚀 Features

- 🧠 Multiple specialized AI agents working in parallel
- 🔍 Autonomous web research and data gathering
- 🔗 Intelligent agent pipeline and task delegation
- 🛠️ Custom tools for enhanced agent capabilities
- ⚡ Fast and efficient multi-step reasoning
- 📊 Structured research output and summarization

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | Agent framework & chaining |
| OpenAI / Gemini | LLM for agent reasoning |
| Tavily | Web search & research tool |
| Python | Core language |

---

## 📁 Project Structure

```
Multi-Agent-Research/
│
├── app.py                  # Main application entry point
├── agents.py               # Agent definitions and configurations
├── pipeline.py             # Multi-agent pipeline orchestration
├── tools.py                # Custom tools available to agents
├── requirements.txt        # Project dependencies
├── .env.example            # Environment variable template
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/Multi-Agent-Research.git
cd Multi-Agent-Research
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```

Activate it:
- **Windows:** `.venv\Scripts\activate`
- **Mac/Linux:** `source .venv/bin/activate`

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```
Then fill in your actual API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

### 5. Run the Application
```bash
python app.py
```

---

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | Your OpenAI API key |
| `LANGCHAIN_API_KEY` | Your LangChain API key |
| `TAVILY_API_KEY` | Your Tavily search API key |

> ⚠️ Never commit your `.env` file to GitHub. It is already added to `.gitignore`.

---

## 📝 How It Works

```
User Research Query
        ↓
   Orchestrator Agent
        ↓
  ┌─────┴──────┐
  ↓            ↓
Research     Analysis
 Agent        Agent
  ↓            ↓
Web Search   Data Processing
  ↓            ↓
  └─────┬──────┘
        ↓
  Pipeline Aggregation
        ↓
  Final Research Report
```

1. **Input** — User submits a research query
2. **Orchestrate** — Main agent breaks the task into subtasks
3. **Research** — Research agent searches the web for information
4. **Analyze** — Analysis agent processes and filters results
5. **Tools** — Custom tools assist agents with specific tasks
6. **Pipeline** — Results flow through the pipeline and get combined
7. **Output** — A comprehensive, structured research report is generated

---

## 🤖 Agents Overview

| Agent | Role |
|-------|------|
| Orchestrator | Plans and delegates tasks to other agents |
| Research Agent | Searches and gathers information from the web |
| Analysis Agent | Processes, filters, and summarizes findings |
| Tools Agent | Uses custom tools for specific operations |

---

## 🛠️ Available Tools

Defined in `tools.py`, agents have access to:
- 🌐 Web search via Tavily
- 📄 Document summarization
- 🔎 Content extraction and filtering
- 📊 Data structuring and formatting

---

## 📦 Requirements

See `requirements.txt` for the full list. Main dependencies:
```
langchain
langchain-openai
tavily-python
python-dotenv
```

---

## 🧪 Running Tests

```bash
python -m pytest
```

---

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feat/your-feature`)
3. Commit your changes (`git commit -m "feat: add your feature"`)
4. Push to the branch (`git push origin feat/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [your-linkedin](https://linkedin.com/in/your-linkedin)
