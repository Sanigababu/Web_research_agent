import streamlit as st
from agent import run_agent

# Title for the app
st.title("🧠 Free Web Research Agent")

# Initialize session state for conversation history if not already initialized
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Display previous conversations
for message in st.session_state['history']:
    st.write(f"USER: {message['user']}")
    st.write(f"AGENT: {message['model']}")

# User query input
query = st.text_input("Ask your question:")

# When the "Run Agent" button is pressed
if st.button("Run Agent") and query:
    with st.spinner("Gathering info..."):
        # Print debug message to terminal
        print("Agent Triggered!")
        
        # Add user query to conversation history
        st.session_state['history'].append({"user": query, "model": "..."})
        
        # Run the agent to get the result
        result = run_agent(query)
        
        # Update the conversation history with the model's response
        st.session_state['history'][-1]['model'] = result
        
        # Display the result in the app
        print("✅ Agent Response:", result)
        st.markdown(result)

