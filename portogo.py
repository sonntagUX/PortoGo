import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("PortoGo: Moving to Portugal Made Simple")
st.write("Ask me anything about relocating from the U.S. to Portugal!")

user_input = st.text_input("How can I help you today?")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a friendly relocation assistant that helps Americans move to Portugal."},
                    {"role": "user", "content": user_input}
                ]
            )
            st.success(response.choices[0].message.content)
        except Exception as e:
            st.error(f"Oops, something went wrong: {e}")
