from openai import OpenAI
import streamlit as st

st.title("PortoGo: Moving to Portugal Made Simple")
st.write("Choose a question to learn more about moving from the U.S. to Portugal:")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Preset questions
questions = [
    "What visas are available for Americans moving to Portugal?",
    "What is the cost of living in Lisbon compared to Los Angeles, CA?",
    "Can I work remotely from Portugal?",
    "How do I find housing in Portugal?",
    "What is the healthcare system like in Portugal?"
]

# Display question buttons
selected_prompt = None
for question in questions:
    if st.button(question):
        selected_prompt = question
        break

# Generate response if a button was clicked
if selected_prompt:
    st.session_state.messages.append({"role": "user", "content": selected_prompt})
    with st.chat_message("user"):
        st.markdown(selected_prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})
