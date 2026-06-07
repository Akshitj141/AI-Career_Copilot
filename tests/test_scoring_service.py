from app.models.resume_model import (
    ContactInfo
)

from app.services.scoring_service import (
    ScoringService
)


def test_score_generation():

    service = ScoringService()

    contact = ContactInfo(
        email="test@test.com",
        phone="9999999999",
        linkedin="linkedin",
        github="github"
    )

    sections = {
        "projects": True,
        "experience": True
    }

    skills = [
        "Python",
        "SQL",
        "Git"
    ]

    report = service.calculate_scores(
        contact,
        sections,
        skills,
        80
    )

    assert report.ats_score > 0

    assert (
        report.career_readiness_score
        > 0
    )