import streamlit as st

st.title("PortoGo: Business Path to Residency in Portugal")
st.write("Hi there! Let’s see if a business-based visa to Portugal might be a good fit for you.")

step = st.session_state.get("step", 0)

def select_option(key, options):
    # Display buttons horizontally and detect clicks
    cols = st.columns(len(options))
    for i, option in enumerate(options):
        if cols[i].button(option):
            st.session_state[key] = option
            return option
    return st.session_state.get(key, None)

if step == 0:
    st.write("First, tell me…")
    selected = select_option("business_intent", ["Yes", "No", "Not Sure"])
    if selected:
        st.session_state.step = 1

elif step == 1:
    st.write("Your previous answer:", st.session_state.get("business_intent", ""))
    
    if st.session_state.business_intent == "Yes":
        selected = select_option("business_type", ["Yes, I’ll run a business", "Yes, I’m a freelancer", "No, I’m investing only"])
        if selected:
            st.session_state.step = 2
    else:
        st.write("That’s okay! There are other visa options depending on your situation — like employment, retirement, study, or family reunification.")

elif step == 2:
    if st.session_state.business_type in ["Yes, I’ll run a business", "Yes, I’m a freelancer"]:
        st.write("Sounds like the D2 Visa might be right for you.")
        st.write("To move forward, I need to ask a few things:")

        business_plan = select_option("business_plan", ["Yes", "No"])
        funds = select_option("funds", ["Yes", "No"])
        living = select_option("living", ["Yes", "No"])

        # Show previous answers
        st.write("Your answers:")
        st.write(f"Business plan: {st.session_state.get('business_plan', '')}")
        st.write(f"Funds: {st.session_state.get('funds', '')}")
        st.write(f"Living in Portugal: {st.session_state.get('living', '')}")

        if business_plan and funds and living:
            st.session_state.step = 3

    elif st.session_state.business_type == "No, I’m investing only":
        investment = select_option("investment", ["Yes", "No"])
        if investment:
            st.session_state.step = 4

elif step == 3:
    if st.session_state.business_plan == "Yes" and st.session_state.funds == "Yes" and st.session_state.living == "Yes":
        st.success("✅ Perfect. You’re likely a good fit for the D2 Entrepreneur Visa.")
    elif st.session_state.funds == "No":
        st.warning("The D2 visa requires financial stability. You may want to secure funding before applying.")
    else:
        st.info("You may need to meet all the conditions to qualify. Want to explore another path?")

elif step == 4:
    if st.session_state.investment == "Yes":
        st.success("✅ Excellent. You may qualify for the Golden Visa.")
    else:
        st.warning("The Golden Visa requires large investments. You may want to explore other visa options.")
