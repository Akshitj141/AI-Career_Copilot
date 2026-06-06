from app.services.skill_service import SkillService


def test_skill_extraction():

    sample_text = """
    Experienced in Python, SQL,
    Machine Learning and Git.
    """

    service = SkillService()

    skills = service.extract_skills(sample_text)

    assert "Python" in skills
    assert "SQL" in skills
    assert "Machine Learning" in skills
    assert "Git" in skills