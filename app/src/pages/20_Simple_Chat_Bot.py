import streamlit as st

# Page configuration
st.set_page_config(page_title="Sample Chat Bot", page_icon="🤖")
import logging

# Logging setup
logging.basicConfig(format="%(filename)s::%(lineno)s::%(levelname)s --> %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Chatbot logic starts here
st.title("Welcome to the Chatbot 🤖")

# Add a button to navigate back to the home page
if st.button("🏠 Back to Home"):
    st.switch_page("Home.py") 

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display chat history
for message in st.session_state.chat_history:
    st.write(message)

# Input box for user messages
user_input = st.text_input("Type your message here:", key="chat_input")

if st.button("Send"):
    if user_input.strip():
        # Placeholder chatbot response
        bot_response = f"Bot: I received your message '{user_input}'. How can I help further?"
        st.session_state.chat_history.append(f"You: {user_input}")
        st.session_state.chat_history.append(bot_response)

# Add a button to reset chat history
if st.button("Reset Chat"):
    st.session_state.chat_history = []  
    st.write("Chat history has been cleared!") 

