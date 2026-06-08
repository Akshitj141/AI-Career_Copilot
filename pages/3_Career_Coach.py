import streamlit as st

from app.services.gemini_service import (
    GeminiService
)

from app.models.job_match_model import (
    JobMatchReport
)

st.title("🧠 AI Career Coach")

if "resume_text" not in st.session_state:

    st.warning(
        "Please upload a resume from the Home page first."
    )

    st.stop()

resume_text = st.session_state[
    "resume_text"
]

st.info(
    "Generate AI-powered resume strengths, weaknesses, and improvement suggestions."
)

if st.button(
    "Generate Career Insights"
):

    gemini_service = GeminiService()

    empty_match_report = (
        JobMatchReport()
    )

    with st.spinner(
        "Generating AI insights..."
    ):

        insights = (
            gemini_service
            .generate_career_insights(
                resume_text,
                empty_match_report
            )
        )

    st.divider()

    st.write(
        insights
    )