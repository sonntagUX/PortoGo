import streamlit as st
import requests

st.title("PortoGo (Powered by Hugging Face)")
st.write("Ask me anything about relocating from the U.S. to Portugal!")

user_input = st.text_input("How can I help you today?")

if user_input:
    with st.spinner("Thinking..."):
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
        headers = {"Authorization": f"Bearer {st.secrets['huggingface']['api_token']}"}
        prompt = f"""### Instruction:\nYou are a friendly relocation assistant that helps Americans move to Portugal.\n### Input:\n{user_input}\n### Response:"""

        response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
        if response.status_code == 200:
            output = response.json()[0]["generated_text"]
            st.success(output.split("### Response:")[-1].strip())
        else:
            st.error("Failed to get a response. Please try again later.")
