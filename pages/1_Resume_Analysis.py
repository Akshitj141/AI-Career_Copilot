import streamlit as st

from app.services.scoring_service import (
    ScoringService
)

st.title("📄 Resume Analysis")

if "resume_text" not in st.session_state:

    st.warning(
        "Please upload a resume from the Home page first."
    )

    st.stop()

resume_stats = st.session_state[
    "resume_stats"
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

scoring_service = ScoringService()

score_report = (
    scoring_service.calculate_scores(
        contact_info,
        sections,
        skills
    )
)

st.subheader(
    "📊 Resume Statistics"
)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Pages",
        resume_stats["pages"]
    )

with col2:

    st.metric(
        "Words",
        resume_stats["words"]
    )

with col3:

    st.metric(
        "Characters",
        resume_stats["characters"]
    )

st.divider()

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

    st.write(
        skills
    )

else:

    st.warning(
        "No skills detected"
    )

st.divider()

st.subheader(
    "📈 ATS Dashboard"
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "ATS Score",
        f"{score_report.ats_score}/100"
    )

with col2:

    st.metric(
        "Career Readiness Score",
        f"{score_report.career_readiness_score}/100"
    )

st.subheader(
    "💡 Recommendations"
)

if score_report.recommendations:

    for recommendation in (
        score_report.recommendations
    ):

        st.warning(
            recommendation
        )

else:

    st.success(
        "Strong Resume Structure"
    )