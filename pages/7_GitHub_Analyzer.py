import streamlit as st

from app.services.github_service import (
    GitHubService
)

st.title("🐙 GitHub Analyzer")

st.info(
    "Analyze your GitHub profile and evaluate project activity."
)

username = st.text_input(
    "GitHub Username",
    placeholder="Example: Akshitj141"
)

if st.button(
    "Analyze GitHub Profile"
):

    if not username:

        st.warning(
            "Please enter a GitHub username."
        )

    else:

        github_service = (
            GitHubService()
        )

        with st.spinner(
            "Analyzing GitHub profile..."
        ):

            profile = (
                github_service
                .analyze_profile(
                    username
                )
            )

        if not profile.username:

            st.error(
                "GitHub profile not found."
            )

        else:

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "GitHub Score",
                    profile.github_score
                )

            with col2:

                st.metric(
                    "Public Repositories",
                    profile.public_repos
                )

            st.divider()

            col1, col2 = st.columns(2)

            with col1:

                st.metric(
                    "Followers",
                    profile.followers
                )

            with col2:

                st.metric(
                    "Following",
                    profile.following
                )

            st.divider()

            st.subheader(
                "💻 Top Languages"
            )

            if profile.top_languages:

                st.write(
                    profile.top_languages
                )

            else:

                st.warning(
                    "No languages detected."
                )

            st.divider()

            st.subheader(
                "💡 Recommendations"
            )

            if profile.public_repos < 5:

                st.warning(
                    "Build more public projects."
                )

            elif profile.public_repos < 10:

                st.info(
                    "Consider adding more projects to strengthen your portfolio."
                )

            else:

                st.success(
                    "Strong repository count."
                )

            if (
                "Python"
                not in profile.top_languages
            ):

                st.warning(
                    "Consider adding Python-based projects."
                )

            if profile.followers < 10:

                st.info(
                    "Increase visibility by contributing to open-source projects."
                )