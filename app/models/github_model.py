from dataclasses import dataclass, field


@dataclass
class GitHubProfile:

    username: str = ""

    public_repos: int = 0

    followers: int = 0

    following: int = 0

    top_languages: list[str] = field(
        default_factory=list
    )

    github_score: float = 0.0