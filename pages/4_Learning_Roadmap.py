import streamlit as st

from app.services.roadmap_service import (
    RoadmapService
)

st.title("🗺 Learning Roadmap")

if "skills" not in st.session_state:

    st.warning(
        "Please upload a resume from the Home page first."
    )

    st.stop()

skills = st.session_state[
    "skills"
]

st.info(
    "Generate a personalized learning roadmap based on your current skills and target role."
)

target_role = st.text_input(
    "Target Role",
    placeholder="Example: AI Engineer Intern"
)

if st.button(
    "Generate Learning Roadmap"
):

    if not target_role:

        st.warning(
            "Please enter a target role."
        )

    else:

        roadmap_service = (
            RoadmapService()
        )

        with st.spinner(
            "Generating roadmap..."
        ):

            roadmap = (
                roadmap_service
                .generate_roadmap(
                    target_role,
                    skills,
                    []
                )
            )

        st.divider()

        st.write(
            roadmap
        )