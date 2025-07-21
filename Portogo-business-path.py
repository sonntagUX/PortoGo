import streamlit as st

# Initialize state variables
if "step" not in st.session_state:
    st.session_state.step = 0
if "path_choice" not in st.session_state:
    st.session_state.path_choice = ""

# Step 0: Offer paths with inline icon and question
if st.session_state.step == 0:
    col_icon, col_text = st.columns([1, 6])
    with col_icon:
        st.image("galo.png", width=100)
    with col_text:
        st.write("Do you plan to move to Portugal by starting a business, working independently, or investing?")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Start a Business"):
            st.session_state.path_choice = "business"
            st.session_state.step = 1
    with col2:
        if st.button("Freelance / Independent Work"):
            st.session_state.path_choice = "freelance"
            st.session_state.step = 1
    with col3:
        if st.button("Invest in Portugal"):
            st.session_state.path_choice = "invest"
            st.session_state.step = 1

# Step 1: Show selected path
elif st.session_state.step == 1:
    col_icon, col_text = st.columns([1, 6])
    with col_icon:
        st.image("galo.png", width=100)
    with col_text:
        st.write(f"You selected: **{st.session_state.path_choice.capitalize()}**")
        st.write("Let's continue from here...")
