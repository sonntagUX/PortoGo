import streamlit as st

st.title("PortoGo: Business Path to Residency in Portugal")
st.write("Hi there! Let’s see if a business-based visa to Portugal might be a good fit for you.")

step = st.session_state.get("step", 0)

if step == 0:
    st.write("First, tell me…")
    response = st.radio("Do you plan to start a business, work independently, or invest in Portugal?", ["Yes", "No", "Not Sure"])
    if st.button("Next"):
        st.session_state.business_intent = response
        st.session_state.step = 1
        st.experimental_rerun()

elif step == 1:
    if st.session_state.business_intent == "Yes":
        response = st.radio("Will you be running a business or working as a freelancer in Portugal?", ["Yes, I’ll run a business", "Yes, I’m a freelancer", "No, I’m investing only"])
        if st.button("Next"):
            st.session_state.business_type = response
            st.session_state.step = 2
            st.experimental_rerun()
    else:
        st.write("That’s okay! There are other visa options depending on your situation — like employment, retirement, study, or family reunification. Want to explore those instead?")

elif step == 2:
    if st.session_state.business_type in ["Yes, I’ll run a business", "Yes, I’m a freelancer"]:
        st.write("Sounds like the D2 Visa might be right for you.")
        st.write("To move forward, I need to ask a few things:")
        business_plan = st.radio("Do you have a business idea or plan already in mind?", ["Yes", "No"])
        funds = st.radio("Can you show access to around €5,000–€10,000 to support your activity or set up your company?", ["Yes", "No"])
        living = st.radio("Will you be living in Portugal full time?", ["Yes", "No"])
        if st.button("Next"):
            st.session_state.business_plan = business_plan
            st.session_state.funds = funds
            st.session_state.living = living
            st.session_state.step = 3
            st.experimental_rerun()
    elif st.session_state.business_type == "No, I’m investing only":
        investment = st.radio("Do you have at least €250,000 to invest in a Portuguese fund, business, or cultural initiative?", ["Yes", "No"])
        if st.button("Next"):
            st.session_state.investment = investment
            st.session_state.step = 4
            st.experimental_rerun()

elif step == 3:
    if st.session_state.business_plan == "Yes" and st.session_state.funds == "Yes" and st.session_state.living == "Yes":
        st.success("✅ Perfect. You’re likely a good fit for the D2 Entrepreneur Visa.")
        st.write("This visa is for people who want to:")
        st.markdown("- Start a business")
        st.markdown("- Provide services as a freelancer")
        st.markdown("- Contribute economically to Portugal")
        st.write("Let’s keep going with paperwork and location details when you’re ready.")
    elif st.session_state.funds == "No":
        st.warning("The D2 visa does require that you show some financial stability — not huge amounts, but enough to prove your business can function. You may want to pause and secure funding before applying.")
    else:
        st.info("You may need to meet all the conditions to qualify. Want to explore another path?")

elif step == 4:
    if st.session_state.investment == "Yes":
        st.success("✅ Excellent. You may qualify for the Golden Visa.")
        st.write("This allows residency with minimal time spent in Portugal and can lead to citizenship after five years.")
        st.write("You can invest in:")
        st.markdown("- Government-approved investment funds (€500K+)")
        st.markdown("- Cultural or scientific projects (€250K+)")
        st.markdown("- Companies that create jobs")
        st.write("Would you like to learn more about each option?")
    else:
        st.warning("The Golden Visa is only available to people making large investments. If that’s not your path, we can look at other options like work-based or family reunification visas.")
