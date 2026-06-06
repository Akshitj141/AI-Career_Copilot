from app.services.jd_service import (
    JDService
)


def test_jd_matching():

    resume_text = """
    Python
    Git
    """

    jd_text = """
    Python
    Git
    TensorFlow
    Docker
    AWS
    Machine Learning
    """

    service = JDService()

    report = service.analyze_match(
        resume_text,
        jd_text
    )

    assert report.match_percentage == 33.33

    assert "Python" in report.matched_skills

    assert "TensorFlow" in report.missing_skills

    assert len(
        report.high_priority_skills
    ) > 0