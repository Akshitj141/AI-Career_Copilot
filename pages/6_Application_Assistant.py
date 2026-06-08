import streamlit as st

from app.services.application_service import (
    ApplicationService
)

st.title("📨 Application Assistant")

if "resume_text" not in st.session_state:

    st.warning(
        "Please upload a resume from the Home page first."
    )

    st.stop()

resume_text = st.session_state[
    "resume_text"
]

company_name = st.text_input(
    "Company Name"
)

jd_text = st.text_area(
    "Paste Job Description",
    height=200
)

st.info(
    "Generate cover letters, referral requests, cold emails, and LinkedIn outreach messages."
)

if st.button(
    "Generate Application Assets"
):

    if not company_name:

        st.warning(
            "Please enter a company name."
        )

    else:

        application_service = (
            ApplicationService()
        )

        with st.spinner(
            "Generating application assets..."
        ):

            assets = (
                application_service
                .generate_application_assets(
                    resume_text,
                    jd_text,
                    company_name
                )
            )

        st.divider()

        st.write(
            assets
        )