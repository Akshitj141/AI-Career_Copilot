import streamlit as st

from app.services.jd_service import (
    JDService
)

from app.services.scoring_service import (
    ScoringService
)

st.title("🎯 Job Description Matching")

if "resume_text" not in st.session_state:

    st.warning(
        "Please upload a resume from the Home page first."
    )

    st.stop()

resume_text = st.session_state[
    "resume_text"
]

contact_info = st.session_state[
    "contact_info"
]

sections = st.session_state[
    "sections"
]

skills = st.session_state[
    "skills"
]

jd_service = JDService()

scoring_service = ScoringService()

jd_text = st.text_area(
    "Paste Job Description",
    height=250
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

    score_report = (
        scoring_service.calculate_scores(
            contact_info,
            sections,
            skills,
            report.match_percentage
        )
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.metric(
            "Job Match Score",
            f"{report.match_percentage}%"
        )

    with col2:

        st.metric(
            "Career Readiness Score",
            f"{score_report.career_readiness_score}/100"
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader(
            "✅ Matched Skills"
        )

        if report.matched_skills:

            st.write(
                report.matched_skills
            )

        else:

            st.warning(
                "No matched skills found."
            )

    with col2:

        st.subheader(
            "❌ Missing Skills"
        )

        if report.missing_skills:

            st.write(
                report.missing_skills
            )

        else:

            st.success(
                "No missing skills detected."
            )

    st.divider()

    st.subheader(
        "🔥 High Priority Skills"
    )

    if report.high_priority_skills:

        for skill in (
            report.high_priority_skills
        ):

            st.error(skill)

    else:

        st.success(
            "No critical skill gaps."
        )

    st.subheader(
        "⚠ Medium Priority Skills"
    )

    if report.medium_priority_skills:

        for skill in (
            report.medium_priority_skills
        ):

            st.warning(skill)

    st.subheader(
        "ℹ Low Priority Skills"
    )

    if report.low_priority_skills:

        for skill in (
            report.low_priority_skills
        ):

            st.info(skill)