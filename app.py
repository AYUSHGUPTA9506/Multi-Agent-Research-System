import streamlit as st
import time
from pipeline import run_research_pipeline

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Multi-Agent Research System",
    page_icon="🔍",
    layout="wide"
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

    /* Base */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background-color: #0D0F14;
        color: #E2E8F0;
    }

    /* Hero Header */
    .hero {
        text-align: center;
        padding: 3rem 1rem 2rem 1rem;
        border-bottom: 1px solid #1E2330;
        margin-bottom: 2.5rem;
    }

    .hero-badge {
        display: inline-block;
        background: linear-gradient(135deg, #1a3a5c, #0f2a47);
        border: 1px solid #2563EB44;
        color: #60A5FA;
        font-size: 0.7rem;
        font-weight: 600;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        padding: 0.35rem 1rem;
        border-radius: 100px;
        margin-bottom: 1.2rem;
    }

    .hero-title {
        font-size: 2.8rem;
        font-weight: 700;
        letter-spacing: -0.03em;
        line-height: 1.15;
        background: linear-gradient(135deg, #E2E8F0 30%, #60A5FA 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.8rem;
    }

    .hero-sub {
        color: #64748B;
        font-size: 1rem;
        font-weight: 400;
        max-width: 520px;
        margin: 0 auto;
        line-height: 1.6;
    }

    /* Pipeline Steps */
    .pipeline-track {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 0;
        margin: 1.5rem 0 2rem 0;
        flex-wrap: wrap;
    }

    .step-node {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-size: 0.78rem;
        font-weight: 500;
        border: 1px solid #1E2330;
        background: #131720;
        color: #64748B;
        transition: all 0.3s ease;
        white-space: nowrap;
    }

    .step-node.active {
        border-color: #2563EB55;
        background: #0f1e35;
        color: #60A5FA;
    }

    .step-node.done {
        border-color: #16653055;
        background: #0d2218;
        color: #4ADE80;
    }

    .step-arrow {
        color: #1E2330;
        font-size: 1rem;
        padding: 0 0.2rem;
    }

    /* Input Area */
    .input-section {
        max-width: 700px;
        margin: 0 auto 2.5rem auto;
    }

    .stTextInput > div > div > input {
        background-color: #131720 !important;
        border: 1px solid #1E2330 !important;
        border-radius: 10px !important;
        color: #E2E8F0 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 0.95rem !important;
        padding: 0.85rem 1.1rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #2563EB !important;
        box-shadow: 0 0 0 3px #2563EB1a !important;
    }

    .stTextInput > div > div > input::placeholder {
        color: #334155 !important;
    }

    /* Button */
    .stButton > button {
        background: linear-gradient(135deg, #1d4ed8, #2563EB) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.75rem 2.5rem !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.02em !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #1e40af, #1d4ed8) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 20px #2563EB33 !important;
    }

    /* Status Log */
    .status-log {
        background: #0A0C10;
        border: 1px solid #1E2330;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.78rem;
        margin-bottom: 1.5rem;
        min-height: 80px;
        line-height: 1.8;
    }

    .log-line { color: #64748B; }
    .log-line.active { color: #60A5FA; }
    .log-line.done { color: #4ADE80; }
    .log-line.error { color: #F87171; }

    /* Result Cards */
    .result-card {
        background: #131720;
        border: 1px solid #1E2330;
        border-radius: 14px;
        padding: 1.5rem;
        margin-bottom: 1.2rem;
    }

    .result-card-header {
        display: flex;
        align-items: center;
        gap: 0.6rem;
        margin-bottom: 1rem;
        padding-bottom: 0.8rem;
        border-bottom: 1px solid #1E2330;
    }

    .result-card-title {
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #94A3B8;
    }

    .score-badge {
        display: inline-block;
        background: linear-gradient(135deg, #16653088, #14532d88);
        border: 1px solid #4ADE8044;
        color: #4ADE80;
        font-size: 1.1rem;
        font-weight: 700;
        padding: 0.3rem 0.9rem;
        border-radius: 8px;
        font-family: 'JetBrains Mono', monospace;
        float: right;
    }

    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        background: #0D0F14;
        border-bottom: 1px solid #1E2330;
        gap: 0.5rem;
    }

    .stTabs [data-baseweb="tab"] {
        background: transparent;
        color: #64748B;
        border-radius: 8px 8px 0 0;
        padding: 0.6rem 1.2rem;
        font-size: 0.85rem;
        font-weight: 500;
    }

    .stTabs [aria-selected="true"] {
        background: #131720 !important;
        color: #E2E8F0 !important;
        border-bottom: 2px solid #2563EB !important;
    }

    /* Divider */
    hr {
        border-color: #1E2330 !important;
    }

    /* Spinner override */
    .stSpinner > div {
        border-top-color: #2563EB !important;
    }

    /* Expander */
    .streamlit-expanderHeader {
        background: #131720 !important;
        border: 1px solid #1E2330 !important;
        border-radius: 10px !important;
        color: #94A3B8 !important;
        font-size: 0.82rem !important;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #1E2330;
        font-size: 0.75rem;
        padding: 2rem 0 1rem 0;
        border-top: 1px solid #131720;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)


# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <div class="hero-badge">🤖 Multi-Agent AI System</div>
    <div class="hero-title">Research Intelligence<br>Platform</div>
    <div class="hero-sub">Four AI agents working in sequence — search, scrape, write, and critique — to deliver structured research reports on any topic.</div>
</div>
""", unsafe_allow_html=True)

# ── Pipeline Visual ───────────────────────────────────────────────────────────
def render_pipeline(active_step=0, done_steps=set()):
    steps = [
        ("🔍", "Search Agent"),
        ("📄", "Reader Agent"),
        ("✍️", "Writer Chain"),
        ("🎯", "Critic Chain"),
    ]
    html = '<div class="pipeline-track">'
    for i, (icon, label) in enumerate(steps):
        if i in done_steps:
            cls = "done"
        elif i == active_step:
            cls = "active"
        else:
            cls = ""
        html += f'<div class="step-node {cls}">{icon} {label}</div>'
        if i < len(steps) - 1:
            html += '<div class="step-arrow">→</div>'
    html += '</div>'
    return html

pipeline_placeholder = st.empty()
pipeline_placeholder.markdown(render_pipeline(-1, set()), unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="input-section">', unsafe_allow_html=True)
col1, col2 = st.columns([5, 1])
with col1:
    topic = st.text_input(
        label="topic",
        label_visibility="collapsed",
        placeholder="Enter a research topic — e.g. Impact of AI on financial markets",
        key="topic_input"
    )
with col2:
    run_btn = st.button("Research →", key="run")
st.markdown('</div>', unsafe_allow_html=True)

# ── Example Topics ────────────────────────────────────────────────────────────
with st.expander("💡 Example topics"):
    examples = [
        "Impact of war on the global stock market",
        "Latest developments in quantum computing 2025",
        "How does inflation affect real estate prices",
        "Breakthroughs in cancer immunotherapy research",
        "The rise of agentic AI systems in enterprise",
    ]
    for ex in examples:
        if st.button(f"→ {ex}", key=ex):
            st.session_state["topic_input"] = ex
            st.rerun()

# ── Run Pipeline ──────────────────────────────────────────────────────────────
if run_btn and topic.strip():
    st.markdown("---")

    log_placeholder = st.empty()
    logs = []

    def update_log(msg, status="log"):
        logs.append((msg, status))
        html = '<div class="status-log">'
        for line, s in logs:
            html += f'<div class="log-line {s}">{"▶" if s == "active" else "✓" if s == "done" else "✗" if s == "error" else "·"} {line}</div>'
        html += '</div>'
        log_placeholder.markdown(html, unsafe_allow_html=True)

    done = set()

    try:
        # Step 1
        pipeline_placeholder.markdown(render_pipeline(0, done), unsafe_allow_html=True)
        update_log("Search Agent — finding recent reliable information...", "active")
        time.sleep(0.3)

        from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

        search_agent = build_search_agent()
        search_result = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
        })
        search_results = search_result['messages'][-1].content
        done.add(0)
        update_log("Search Agent — complete", "done")

        # Step 2
        pipeline_placeholder.markdown(render_pipeline(1, done), unsafe_allow_html=True)
        update_log("Reader Agent — scraping top resources...", "active")
        time.sleep(0.3)

        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{search_results[:800]}"
            )]
        })
        scraped_content = reader_result['messages'][-1].content
        done.add(1)
        update_log("Reader Agent — complete", "done")

        # Step 3
        pipeline_placeholder.markdown(render_pipeline(2, done), unsafe_allow_html=True)
        update_log("Writer Chain — drafting structured report...", "active")
        time.sleep(0.3)

        research_combined = (
            f"SEARCH RESULTS:\n{search_results}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{scraped_content}"
        )
        report = writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })
        done.add(2)
        update_log("Writer Chain — report drafted", "done")

        # Step 4
        pipeline_placeholder.markdown(render_pipeline(3, done), unsafe_allow_html=True)
        update_log("Critic Chain — evaluating report quality...", "active")
        time.sleep(0.3)

        feedback = critic_chain.invoke({"report": report})
        done.add(3)
        update_log("Critic Chain — review complete", "done")

        # All done
        pipeline_placeholder.markdown(render_pipeline(-1, done), unsafe_allow_html=True)
        update_log("All agents complete — results ready below ✓", "done")

        # ── Results ───────────────────────────────────────────────────────────
        st.markdown("---")
        st.markdown("### Results")

        tab1, tab2, tab3 = st.tabs(["📋 Final Report", "🎯 Critic Feedback", "🔎 Raw Data"])

        with tab1:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-card-header">
                    <span>✍️</span>
                    <span class="result-card-title">Research Report — {topic}</span>
                </div>
            """, unsafe_allow_html=True)
            st.markdown(report)
            st.markdown("</div>", unsafe_allow_html=True)

            st.download_button(
                label="⬇ Download Report (.md)",
                data=report,
                file_name=f"report_{topic[:30].replace(' ', '_')}.md",
                mime="text/markdown"
            )

        with tab2:
            # Try to extract score for badge
            score_line = ""
            for line in feedback.split("\n"):
                if "Score:" in line or "score:" in line:
                    score_line = line.strip()
                    break

            st.markdown(f"""
            <div class="result-card">
                <div class="result-card-header">
                    <span>🎯</span>
                    <span class="result-card-title">Critic Review</span>
                    {"<span class='score-badge'>" + score_line + "</span>" if score_line else ""}
                </div>
            """, unsafe_allow_html=True)
            st.markdown(feedback)
            st.markdown("</div>", unsafe_allow_html=True)

        with tab3:
            with st.expander("🔍 Search Agent Results"):
                st.text(search_results)
            with st.expander("📄 Scraped Content"):
                st.text(scraped_content)

    except Exception as e:
        pipeline_placeholder.markdown(render_pipeline(-1, done), unsafe_allow_html=True)
        update_log(f"Error: {str(e)}", "error")
        st.error(f"**Pipeline failed:** {str(e)}")

elif run_btn and not topic.strip():
    st.warning("Please enter a research topic first.")

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    Multi-Agent Research System · Powered by LangChain + Groq · Built by Ayush Gupta
</div>
""", unsafe_allow_html=True)