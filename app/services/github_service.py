import requests

from app.models.github_model import (
    GitHubProfile
)


class GitHubService:

    def analyze_profile(
        self,
        username: str
    ) -> GitHubProfile:

        user_url = (
            f"https://api.github.com/users/{username}"
        )

        response = requests.get(
            user_url
        )

        if response.status_code != 200:

            return GitHubProfile()

        user_data = response.json()

        repos_url = user_data[
            "repos_url"
        ]

        repos_response = requests.get(
            repos_url
        )

        repos = repos_response.json()

        languages = []

        for repo in repos:

            language = repo.get(
                "language"
            )

            if language:

                languages.append(
                    language
                )

        top_languages = list(
            set(languages)
        )[:5]

        score = min(
            (
                user_data[
                    "public_repos"
                ] * 5
            ),
            100
        )

        return GitHubProfile(
            username=username,
            public_repos=user_data[
                "public_repos"
            ],
            followers=user_data[
                "followers"
            ],
            following=user_data[
                "following"
            ],
            top_languages=top_languages,
            github_score=score
        )