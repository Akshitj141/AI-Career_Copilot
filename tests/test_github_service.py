from app.services.github_service import (
    GitHubService
)


def test_github_service():

    service = GitHubService()

    profile = service.analyze_profile(
        "torvalds"
    )

    assert profile.username == "torvalds"