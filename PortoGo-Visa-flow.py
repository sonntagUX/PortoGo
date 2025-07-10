import streamlit as st
from PIL import Image

st.set_page_config(page_title="PortoGo Relocation Assistant")

# Load CSS style
st.markdown("""
    <style>
    .custom-button {
        box-shadow: inset 0px 1px 0px 0px #ffffff;
        background: linear-gradient(to bottom, #ffffff 5%, #f6f6f6 100%);
        background-color: #ffffff;
        border-radius: 6px;
        border: 1px solid #dcdcdc;
        display: inline-block;
        cursor: pointer;
        color: #666666;
        font-family: Arial, sans-serif;
        font-size: 15px;
        font-weight: bold;
        padding: 6px 24px;
        text-decoration: none;
        text-shadow: 0px 1px 0px #ffffff;
        margin: 10px;
    }
    .custom-button:hover {
        background: linear-gradient(to bottom, #f6f6f6 5%, #ffffff 100%);
        background-color: #f6f6f6;
    }
    </style>
""", unsafe_allow_html=True)

# Logo and intro
logo = Image.open("Portogo-bot-logo.png")
st.image(logo)

st.header("PortoGo")
st.subheader("Visa Eligibility Assistant")
st.text("Let's get started! Please answer the following questions so we can assess your situation and offer the best advice.")

# Session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "relocation_reason" not in st.session_state:
    st.session_state.relocation_reason = None
if "income_range" not in st.session_state:
    st.session_state.income_range = None

# Reset
def reset():
    st.session_state.step = 1
    st.session_state.relocation_reason = None
    st.session_state.income_range = None

st.button("🔄 Restart", on_click=reset)

# STEP 1
if st.session_state.step == 1:
    st.markdown("**Q1. Why are you relocating to Portugal?**")

    with st.form(key="relocation_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            submit_nomad = st.form_submit_button("Digital Nomad")
        with col2:
            submit_retired = st.form_submit_button("Retired")
        with col3:
            submit_family = st.form_submit_button("Family Reunion")

        if submit_nomad:
            st.session_state.relocation_reason = "I am a digital nomad"
            st.session_state.step = 2
        elif submit_retired:
            st.session_state.relocation_reason = "I am retired"
            st.session_state.step = 2
        elif submit_family:
            st.session_state.relocation_reason = "Family reunion"
            st.session_state.step = 2

# STEP 2
if st.session_state.step == 2:
    st.markdown(f"<div style='text-align: left;'>**Q1. Why are you relocating to Portugal?**</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: left; color: green;'>{st.session_state.relocation_reason}</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("**Q2. What is your monthly income or savings? (USD)**")

    with st.form(key="income_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            submit_low = st.form_submit_button("Below $1000")
        with col2:
            submit_mid = st.form_submit_button("1000 - 3000")
        with col3:
            submit_high = st.form_submit_button("Above 3000")

        if submit_low:
            st.session_state.income_range = "Below $1,000"
            st.session_state.step = 3
        elif submit_mid:
            st.session_state.income_range = "$1,000 - $3,000"
            st.session_state.step = 3
        elif submit_high:
            st.session_state.income_range = "Above $3,000"
            st.session_state.step = 3

# STEP 3
if st.session_state.step == 3:
    st.markdown(f"<div style='text-align: left;'>**Q2. What is your monthly income or savings?**</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: left; color: green;'>{st.session_state.income_range}</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### Result:")

    reason = st.session_state.relocation_reason
    income = st.session_state.income_range

    if reason == "I am a digital nomad":
        if income == "Above $3,000":
            st.success("You may qualify for the D8 Digital Nomad Visa. Start gathering proof of remote income.")
        else:
            st.warning("Digital Nomad visa usually requires proof of higher income. You might need a co-sponsor or alternative path.")
    elif reason == "I am retired":
        if income in ["$1,000 - $3,000", "Above $3,000"]:
            st.success("You may qualify for the D7 Retirement Visa. Savings and pension documents will be needed.")
        else:
            st.warning("You may need to show additional financial resources or apply with a co-signer.")
    elif reason == "Family reunion":
        st.success("You may qualify for a Family Reunification Visa. Your sponsor in Portugal must provide documents.")

    st.markdown("*This is a general guide. Please consult the Portuguese consulate for official requirements.*")
