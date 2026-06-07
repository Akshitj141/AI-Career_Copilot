import streamlit as st

from app.services.pdf_service import PDFService
from app.services.parser_service import ParserService
from app.services.skill_service import SkillService


st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Copilot")

st.markdown(
    """
    Welcome to AI Career Copilot.

    Upload your resume once and access:

    - Resume Analysis
    - JD Matching
    - Career Coach
    - Learning Roadmap
    - Interview Preparation
    - Application Assistant
    - GitHub Analyzer

    using the sidebar navigation.
    """
)

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    pdf_service = PDFService()
    parser_service = ParserService()
    skill_service = SkillService()

    result = pdf_service.extract_text(
        uploaded_file
    )

    resume_text = result["text"]

    contact_info = (
        parser_service.extract_contact_info(
            resume_text
        )
    )

    sections = (
        parser_service.identify_sections(
            resume_text
        )
    )

    skills = (
        skill_service.extract_skills(
            resume_text
        )
    )

    st.session_state[
        "resume_text"
    ] = resume_text

    st.session_state[
        "contact_info"
    ] = contact_info

    st.session_state[
        "sections"
    ] = sections

    st.session_state[
        "skills"
    ] = skills

    st.session_state[
        "resume_stats"
    ] = result

    st.success(
        "Resume uploaded successfully."
    )

    st.info(
        "Use the sidebar to access all modules."
    )

else:

    st.warning(
        "Upload a resume to begin."
    )