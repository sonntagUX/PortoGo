# portopal.py
import streamlit as st
import os
from openai import OpenAI

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"]

st.title("PortoGo: Moving to Portugal Made Simple")
st.write("Ask me anything about relocating from the U.S. to Portugal!")

# Capture user input
user_input = st.text_input("How can i help you today?")

# Make API call
if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly relocation assistant that helps Americans move to Portugal."},
                {"role": "user", "content": user_input}
            ]
        )
        st.success(response.choices[0].message.content)
