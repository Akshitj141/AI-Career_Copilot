import streamlit as st

from app.services.pdf_service import PDFService
from app.services.parser_service import ParserService
from app.services.skill_service import SkillService
from app.services.jd_service import JDService

from app.services.gemini_service import GeminiService
from app.services.roadmap_service import RoadmapService
from app.services.interview_service import InterviewService
from app.services.application_service import ApplicationService


st.set_page_config(
    page_title="AI Career Copilot",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI Career Copilot")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    pdf_service = PDFService()
    parser_service = ParserService()
    skill_service = SkillService()
    jd_service = JDService()

    gemini_service = GeminiService()
    roadmap_service = RoadmapService()
    interview_service = InterviewService()
    application_service = ApplicationService()

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

    report = None

    st.success(
        "Resume Processed Successfully"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "📄 Resume Statistics"
        )

        st.metric(
            "Pages",
            result["pages"]
        )

        st.metric(
            "Words",
            result["words"]
        )

    with col2:

        st.subheader(
            "📞 Contact Information"
        )

        st.write(
            "Email:",
            contact_info.email
        )

        st.write(
            "Phone:",
            contact_info.phone
        )

        st.write(
            "LinkedIn:",
            contact_info.linkedin
        )

        st.write(
            "GitHub:",
            contact_info.github
        )

    st.divider()

    st.subheader(
        "📂 Detected Sections"
    )

    if sections:

        for section in sections.keys():

            st.success(
                section.title()
            )

    else:

        st.warning(
            "No sections detected"
        )

    st.divider()

    st.subheader(
        "🛠 Extracted Skills"
    )

    if skills:

        st.write(skills)

    else:

        st.warning(
            "No skills detected"
        )

    st.divider()

    st.subheader(
        "🎯 Job Description Matching"
    )

    jd_text = st.text_area(
        "Paste Job Description",
        height=200
    )

    if st.button(
        "Analyze Match"
    ):

        report = (
            jd_service.analyze_match(
                resume_text,
                jd_text
            )
        )

        st.metric(
            "Match Percentage",
            f"{report.match_percentage}%"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.subheader(
                "✅ Matched Skills"
            )

            st.write(
                report.matched_skills
            )

        with col2:

            st.subheader(
                "❌ Missing Skills"
            )

            st.write(
                report.missing_skills
            )

        st.subheader(
            "🔥 High Priority Skills"
        )

        st.write(
            report.high_priority_skills
        )

    st.divider()

    st.subheader(
        "🧠 AI Career Coach"
    )

    if st.button(
        "Generate Career Insights"
    ):

        insights = (
            gemini_service
            .generate_career_insights(
                resume_text,
                jd_text if jd_text else ""
            )
        )

        st.write(insights)

    st.divider()

    st.subheader(
        "🗺 Learning Roadmap"
    )

    target_role = st.text_input(
        "Target Role"
    )

    if st.button(
        "Generate Roadmap"
    ):

        roadmap = (
            roadmap_service
            .generate_roadmap(
                target_role,
                skills,
                []
            )
        )

        st.write(roadmap)

    st.divider()

    st.subheader(
        "🎤 Interview Preparation"
    )

    if st.button(
        "Generate Interview Questions"
    ):

        questions = (
            interview_service
            .generate_questions(
                resume_text,
                jd_text
            )
        )

        st.write(questions)

    st.divider()

    st.subheader(
        "📨 Application Assistant"
    )

    company_name = st.text_input(
        "Company Name"
    )

    if st.button(
        "Generate Application Assets"
    ):

        assets = (
            application_service
            .generate_application_assets(
                resume_text,
                jd_text,
                company_name
            )
        )

        st.write(assets)