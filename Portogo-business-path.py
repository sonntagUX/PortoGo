import streamlit as st

# Initialize step in session state
if "step" not in st.session_state:
    st.session_state.step = 0

# Step 0: Present three CTA buttons
if st.session_state.step == 0:
    # Create two columns for inline layout
    col_icon, col_text = st.columns([1, 5])  # Adjust width ratio as needed
    
    with col_icon:
        st.image("galo.png", width=100)
    
    with col_text:
        st.write("Do you plan to move to Portugal by starting a business, working independently, or investing?")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("Start a Business"):
            st.session_state.path_choice = "business"
            st.session_state.step = 1
            st.experimental_rerun()
    with col2:
        if st.button("Freelance / Independent Work"):
            st.session_state.path_choice = "freelance"
            st.session_state.step = 1
            st.experimental_rerun()
    with col3:
        if st.button("Invest in Portugal"):
            st.session_state.path_choice = "invest"
            st.session_state.step = 1
            st.experimental_rerun()

elif st.session_state.step == 1:
    st.write(f"You selected: **{st.session_state.path_choice.capitalize()}**")
    st.write("We'll continue from here in the next step.")
