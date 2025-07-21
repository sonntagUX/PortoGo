import streamlit as st

# Load and display the icon
st.image("galo.png", width=100)

# Initialize step in session state
if "step" not in st.session_state:
    st.session_state.step = 0

# Step 0: Present three CTA buttons
if st.session_state.step == 0:
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

# You can add step 1 logic in the next step
elif st.session_state.step == 1:
    st.write(f"You selected: **{st.session_state.path_choice.capitalize()}**")
    # Placeholder for the next question
    st.write("We'll continue from here in the next step.")
