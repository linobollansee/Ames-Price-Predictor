import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - Churned Customer Study" notebook
    st.success(
        f"* We hypothesize that houses with larger square footage tend to "
        f"have a higher value: Correct. "
        f"This is supported by the correlation study in the Housing Prices "
        f"Study. \n\n"
        f"* We hypothesize that houses in better overall condition tend to "
        f"have a higher value: Correct. "
        f"The correlation study in the Housing Prices Study confirms this. "
        f"\n\n"
        f"* We hypothesize that houses with a more recent remodel tend to "
        f"have a higher value: Correct. "
        f"This is also supported by the correlation study in the Housing "
        f"Prices Study. \n\n"
        )
