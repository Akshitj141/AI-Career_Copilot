from app.prompts.interview_prompt import (
    INTERVIEW_PROMPT
)

from app.services.gemini_service import (
    GeminiService
)


class InterviewService:

    def __init__(self):

        self.gemini_service = GeminiService()

    def generate_questions(
        self,
        resume_data,
        jd_text: str
    ):

        prompt = f"""
        {INTERVIEW_PROMPT}

        Resume Data:
        {resume_data}

        Job Description:
        {jd_text}
        """

        response = (
            self.gemini_service
            .model
            .generate_content(prompt)
        )

        return response.text