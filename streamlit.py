import os
os.environ["TORCH_DISABLE_STRUCTURED_LOGGING"] = "1"
os.environ["STREAMLIT_WATCH_USE_POLLING"] = "true"

import streamlit as st
from planner_graph import planner
from langchain_core.runnables import RunnableConfig

st.set_page_config(page_title="Smart Task Planner", page_icon="🧠")

st.title("Smart Task Planner")
st.markdown("Enter a task or project requirement, and I’ll break it down for you.")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Input box
user_input = st.text_area("🔍 What do you want to plan?", placeholder="e.g. Build a Resume Analyzer with frontend, backend, and Docker", height=100)

# Submit
if st.button("Generate Plan") and user_input.strip() != "":
    with st.spinner("Planning your tasks..."):
        try:
            result = planner.invoke({"input": user_input}, config=RunnableConfig())
            st.session_state.history.append({"query": user_input, "result": result["result"]})
            st.success("✅ Plan generated!")
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Display history
if st.session_state.history:
    st.subheader("📝 Previous Plans")
    for entry in reversed(st.session_state.history):
        st.markdown(f"**🧑‍💻 Task:** {entry['query']}")
        st.markdown("**📋 Plan:**")
        st.code(entry["result"], language="markdown")
        st.markdown("---")
