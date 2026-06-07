from dataclasses import dataclass


@dataclass
class ScoreReport:

    ats_score: float = 0.0

    job_match_score: float = 0.0

    career_readiness_score: float = 0.0

    resume_quality_score: float = 0.0

    skill_score: float = 0.0

    project_score: float = 0.0

    experience_score: float = 0.0

    recommendations: list[str] | None = None