from app.services.gemini_service import (
    GeminiService
)

from app.prompts.roadmap_prompt import (
    ROADMAP_PROMPT
)


class RoadmapService:

    def __init__(self):

        self.gemini_service = GeminiService()

    def generate_roadmap(
        self,
        target_role: str,
        current_skills: list[str],
        missing_skills: list[str]
    ):

        prompt = f"""
        {ROADMAP_PROMPT}

        Target Role:
        {target_role}

        Current Skills:
        {current_skills}

        Missing Skills:
        {missing_skills}
        """

        return (
            self.gemini_service
            .model
            .generate_content(prompt)
            .text
        )