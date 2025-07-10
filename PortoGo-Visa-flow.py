import streamlit as st

st.set_page_config(page_title="PortoGo Relocation Assistant", page_icon="🇵🇹")

st.title("🇵🇹 PortoGo Visa Eligibility Assistant")
# Logo
logo = Image.open("portogologo.png")
st.Image(logo, width=200)


# Question 1
st.subheader("Q1. Why are you relocating to Portugal?")
relocation_reason = st.radio(
    "Select one:",
    ["I am a digital nomad", "I am retired", "Family reunion"]
)

# Question 2
st.subheader("Q2. What is your monthly income or savings? (USD)")
income_range = st.radio(
    "Choose your range:",
    ["Below $1,000", "$1,000 - $3,000", "Above $3,000"]
)

# Submit button
if st.button("Get Visa Guidance"):
    st.markdown("### 📝 Result:")
    if relocation_reason == "I am a digital nomad":
        if income_range == "Above $3,000":
            st.success("You may qualify for the D8 Digital Nomad Visa. Start gathering proof of remote income.")
        else:
            st.warning("Digital Nomad visa usually requires proof of higher income. You might need a co-sponsor or alternative path.")
    elif relocation_reason == "I am retired":
        if income_range in ["$1,000 - $3,000", "Above $3,000"]:
            st.success("You may qualify for the D7 Retirement Visa. Savings and pension documents will be needed.")
        else:
            st.warning("You may need to show additional financial resources or apply with a co-signer.")
    elif relocation_reason == "Family reunion":
        st.success("You may qualify for a Family Reunification Visa. Your sponsor in Portugal must provide documents.")

    st.markdown("✅ *This is a general guide. Please consult the Portuguese consulate for official requirements.*")
