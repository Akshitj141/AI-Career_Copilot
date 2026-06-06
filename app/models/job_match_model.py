from dataclasses import dataclass, field


@dataclass
class JobMatchReport:

    matched_skills: list[str] = field(
        default_factory=list
    )

    missing_skills: list[str] = field(
        default_factory=list
    )

    match_percentage: float = 0.0