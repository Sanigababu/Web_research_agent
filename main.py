import streamlit as st
from agent import run_agent

# --- App Title ---
st.set_page_config(page_title="Web Research Agent", page_icon="🧠")
st.title("🧠 Free Web Research Agent")
st.caption("Ask your question, and let the agent browse, read, and summarize the web for you!")

# --- Session State for Conversation History ---
if 'history' not in st.session_state:
    st.session_state['history'] = []

# --- Query Input ---
query = st.text_input("Ask your question:")

# --- Run Agent ---
if st.button("🚀 Run Agent") and query:
    with st.spinner("🧠 Agent is thinking..."):
        try:
            # Log user's query
            st.session_state['history'].append({"user": query, "model": "..."})

            # Get agent's answer
            result = run_agent(query)

            # Update conversation history
            st.session_state['history'][-1]['model'] = result
            st.success("✅ Done!")
        except Exception as e:
            result = f"❌ Agent crashed with error:\n\n```\n{e}\n```"
            st.session_state['history'][-1]['model'] = result
            st.error("Something went wrong!")

# --- Display Conversation History ---
if st.session_state['history']:
    st.markdown("### 📚 Conversation History")
    for i, message in enumerate(reversed(st.session_state['history']), 1):
        with st.expander(f"Q{i}: {message['user']}"):
            st.markdown(message['model'], unsafe_allow_html=True)


