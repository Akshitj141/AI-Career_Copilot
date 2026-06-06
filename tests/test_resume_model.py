from app.models.resume_model import ResumeData


def test_resume_model_creation():
    resume = ResumeData()

    assert resume.contact.name == ""
    assert resume.skills == []
    assert resume.education == []