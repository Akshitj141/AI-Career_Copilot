from app.prompts.application_prompt import (
    APPLICATION_PROMPT
)

from app.services.gemini_service import (
    GeminiService
)


class ApplicationService:

    def __init__(self):

        self.gemini_service = GeminiService()

    def generate_application_assets(
        self,
        resume_data,
        jd_text: str,
        company_name: str
    ):

        prompt = f"""
        {APPLICATION_PROMPT}

        Company:
        {company_name}

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