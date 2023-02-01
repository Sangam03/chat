import streamlit as st

st.title("Chatbot")

user_input = st.text_input("Enter your message:")

responses = {
    "hello": "Hello! How can I help you today?",
    "goodbye": "Goodbye! Have a great day.",
    "thanks": "You're welcome!",
}

if user_input in responses:
    st.write(responses[user_input])
else:
    st.write("I'm sorry, I don't understand what you're saying.")
