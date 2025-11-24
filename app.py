import streamlit as st

from ui.theme import inject_theme
from ui.layout import render_header, render_chat, render_sidebar_plan
from ui.components import input_box, primary_button

from core.research_engine import ResearchEngine
from plan.plan_generator import PlanGenerator
from plan.plan_updater import PlanUpdater
from core.llm_client import LLMClient

def is_off_topic(text: str):
    company_keywords = [
        "company", "industry", "competitor", "market", "revenue", "products",
        "services", "valuation", "ceo", "founder", "headquarters",
        "compare", "business", "profile", "overview", "analysis",
        "eightfold", "eightfold.ai", "talent", "hr", "saas"
    ]
    if any(keyword in text.lower() for keyword in company_keywords):
        return False   # Company-related → ALLOWED
    return True

# STREAMLIT
st.set_page_config(page_title="AI Company Research Assistant", layout="wide")
inject_theme()

# SESSION
if "messages" not in st.session_state:
    st.session_state.messages = []

if "plan" not in st.session_state:
    st.session_state.plan = None

if "update_section" not in st.session_state:
    st.session_state.update_section = None


engine = ResearchEngine()
planner = PlanGenerator()
updater = PlanUpdater()
llm = LLMClient()


with st.sidebar:
    render_sidebar_plan(st.session_state.plan)

render_header()
render_chat(st.session_state.messages)

user_text = input_box()
clicked = primary_button("Search")


def is_company_query(text):
    if "?" in text:
        return False
    if len(text.split()) > 3:
        return False
    if any(x in text.lower() for x in ["who", "what", "is", "are", "tell", "explain"]):
        return False
    return True


# MESSAGE INGESTION
if clicked and user_text.strip():

    # 🔹 CLEAR SEARCH BAR after clicking
    st.session_state["text_input"] = ""  

    # Store user message
    st.session_state.messages.append(("user", user_text))

    last = user_text.strip()

  
    # 1️ UPDATE MODE
    
    if st.session_state.update_section:
        section = st.session_state.update_section
        st.session_state.plan = updater.update_section(st.session_state.plan, section, last)
        st.session_state.update_section = None
        st.session_state.messages.append(("bot", f" Updated {section.replace('_',' ')}."))
        st.rerun()

    
    # 2️ DETECT UPDATE INTENT
    
    if last.lower().startswith("update "):
        sec = None
        for s in updater.VALID_SECTIONS:
            if s.replace("_", " ").lower() in last.lower():
                sec = s
        if not sec:
            st.session_state.messages.append(("bot", " Could not detect section."))
            st.rerun()

        st.session_state.update_section = sec
        st.session_state.messages.append(("bot", f" What should the new text be for {sec.replace('_',' ')}?"))
        st.rerun()


    # Company mode
    if is_company_query(last):
        with st.spinner("Analyzing company…"):
            try:
                info = engine.run(last)
                combined = {
                    "yahoo": info.get("yahoo"),
                    "news": info.get("news"),
                    "wiki": info.get("wiki"),
                }
                plan = planner.generate(last, combined)
                st.session_state.plan = plan
                st.session_state.messages.append(("bot", f" Account plan generated for {last}."))
            except Exception as e:
                st.session_state.messages.append(("bot", f" Error: {str(e)}"))
        st.rerun()

    
    # Reject off-topic questions
    if is_off_topic(last):
        st.session_state.messages.append((
            "bot",
            "I apologize, but I can only answer company-related research queries. "
            "Please enter a company name or a business-related question."
        ))
        st.rerun()

    # If it is NOT off-topic → normal
    reply = llm.run(last)
    st.session_state.messages.append(("bot", reply))
    st.rerun()

