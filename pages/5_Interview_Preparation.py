import streamlit as st

from app.services.interview_service import (
    InterviewService
)

st.title("🎤 Interview Preparation")

if "resume_text" not in st.session_state:

    st.warning(
        "Please upload a resume from the Home page first."
    )

    st.stop()

resume_text = st.session_state[
    "resume_text"
]

jd_text = st.text_area(
    "Paste Job Description (Optional)",
    height=200
)

st.info(
    "Generate personalized interview questions based on your resume and target role."
)

if st.button(
    "Generate Interview Questions"
):

    interview_service = (
        InterviewService()
    )

    with st.spinner(
        "Generating interview questions..."
    ):

        questions = (
            interview_service
            .generate_questions(
                resume_text,
                jd_text
            )
        )

    st.divider()

    st.write(
        questions
    )