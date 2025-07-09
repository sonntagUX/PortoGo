import streamlit as st
from gpt4all import GPT4All

model = GPT4All("gpt4all-lora")

st.title("PortoGo: Moving to Portugal Made Simple")
st.write("Ask me anything about relocating from the U.S. to Portugal!")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a friendly relocation assistant that helps Americans move to Portugal."}
    ]

# Display chat messages from history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user"):
            st.markdown(msg["content"])
    elif msg["role"] == "assistant":
        with st.chat_message("assistant"):
            st.markdown(msg["content"])

# Accept user input
if prompt := st.chat_input("How can I help you today?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        st.markdown("Thinking...")

        # Build prompt for GPT4All: combine system + user messages as plain text
        system_prompt = st.session_state.messages[0]["content"]
        # Use last user message as prompt, or build a longer context if you want
        user_prompt = prompt
        full_prompt = f"{system_prompt}\nUser: {user_prompt}\nAssistant:"

        try:
            response = model.generate(full_prompt)
            # Update last assistant message with real response
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.experimental_rerun()  # Refresh to display new message properly
        except Exception as e:
            st.error(f"Oops, something went wrong: {e}")
