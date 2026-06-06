import os

import google.generativeai as genai

from dotenv import load_dotenv

from app.prompts.career_coach_prompt import (
    CAREER_COACH_PROMPT
)

load_dotenv()


class GeminiService:

    def __init__(self):

        genai.configure(
            api_key=os.getenv(
                "GEMINI_API_KEY"
            )
        )

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash"
        )

    def generate_career_insights(
        self,
        resume_data,
        match_report
    ):

        prompt = f"""
        {CAREER_COACH_PROMPT}

        Resume Data:
        {resume_data}

        Job Match Report:
        {match_report}
        """

        response = self.model.generate_content(
            prompt
        )

        return response.text