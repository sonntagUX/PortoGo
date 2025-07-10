import streamlit as st
from PIL import Image

st.set_page_config(page_title="PortoGo Relocation Assistant")

# Logo and intro
logo = Image.open("Portogo-bot-logo.png")
st.image(logo)

st.header("PortoGo")

st.subheader("Visa Eligibility Assistant")
st.text("Let's get started! Please answer the following questions so we can assess your situation and offer the best advice.")

# Use session state to track progress
if "step" not in st.session_state:
    st.session_state.step = 1
if "relocation_reason" not in st.session_state:
    st.session_state.relocation_reason = None
if "income_range" not in st.session_state:
    st.session_state.income_range = None

# Function to reset
def reset():
    st.session_state.step = 1
    st.session_state.relocation_reason = None
    st.session_state.income_range = None

st.button("🔄 Restart", on_click=reset)

# --- STEP 1: Why are you relocating?
if st.session_state.step == 1:
    st.markdown("**Q1. Why are you relocating to Portugal?**", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("🧑‍💻 Digital Nomad"):
            st.session_state.relocation_reason = "I am a digital nomad"
            st.session_state.step = 2
    with col2:
        if st.button("👵 Retired"):
            st.session_state.relocation_reason = "I am retired"
            st.session_state.step = 2
    with col3:
        if st.button("👨‍👩‍👧 Family Reunion"):
            st.session_state.relocation_reason = "Family reunion"
            st.session_state.step = 2

# --- STEP 2: Income level
if st.session_state.step >= 2:
    st.markdown(f"<div style='text-align: left;'>**Q1. Why are you relocating to Portugal?**</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: right; color: green;'>{st.session_state.relocation_reason}</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("**Q2. What is your monthly income or savings? (USD)**", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("Below $1,000"):
            st.session_state.income_range = "Below $1,000"
            st.session_state.step = 3
    with col2:
        if st.button("$1,000 - $3,000"):
            st.session_state.income_range = "$1,000 - $3,000"
            st.session_state.step = 3
    with col3:
        if st.button("💵 Above $3,000"):
            st.session_state.income_range = "Above $3,000"
            st.session_state.step = 3

# --- STEP 3: Results
if st.session_state.step >= 3:
    st.markdown(f"<div style='text-align: left;'>**Q2. What is your monthly income or savings?**</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: right; color: green;'>{st.session_state.income_range}</div>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("### 📝 Result:")

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

    st.markdown("✅ *This is a general guide. Please consult the Portuguese consulate for official requirements.*")
