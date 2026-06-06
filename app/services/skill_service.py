import json
from pathlib import Path


class SkillService:

    def __init__(self):

        skills_file = (
            Path("data")
            / "skills"
            / "skills_master.json"
        )

        with open(skills_file, "r", encoding="utf-8") as file:
            self.skills_database = json.load(file)["skills"]

    def extract_skills(self, text: str):

        found_skills = []

        text_lower = text.lower()

        for skill in self.skills_database:

            if skill.lower() in text_lower:
                found_skills.append(skill)

        return sorted(list(set(found_skills)))