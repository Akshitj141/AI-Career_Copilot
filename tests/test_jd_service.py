from app.services.jd_service import (
    JDService
)


def test_jd_matching():

    resume_text = """
    Python
    Machine Learning
    Git
    """

    jd_text = """
    Python
    Machine Learning
    TensorFlow
    Docker
    Git
    """

    service = JDService()

    report = service.analyze_match(
        resume_text,
        jd_text
    )

    assert report.match_percentage == 60.0

    assert "Python" in report.matched_skills

    assert "TensorFlow" in report.missing_skills

    assert "Docker" in report.missing_skills
    