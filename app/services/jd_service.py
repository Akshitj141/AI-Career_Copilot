from app.models.job_match_model import (
    JobMatchReport
)

from app.services.skill_service import (
    SkillService
)


class JDService:

    def __init__(self):

        self.skill_service = SkillService()

    def analyze_match(
        self,
        resume_text: str,
        jd_text: str
    ) -> JobMatchReport:

        resume_skills = set(
            self.skill_service.extract_skills(
                resume_text
            )
        )

        jd_skills = set(
            self.skill_service.extract_skills(
                jd_text
            )
        )

        matched_skills = sorted(
            list(
                resume_skills.intersection(
                    jd_skills
                )
            )
        )

        missing_skills = sorted(
            list(
                jd_skills - resume_skills
            )
        )

        if len(jd_skills) == 0:

            match_percentage = 0.0

        else:

            match_percentage = round(
                (
                    len(matched_skills)
                    / len(jd_skills)
                )
                * 100,
                2
            )

        high_priority_skills = missing_skills[:3]

        medium_priority_skills = (
            missing_skills[3:6]
        )

        low_priority_skills = (
            missing_skills[6:]
        )

        return JobMatchReport(
            matched_skills=matched_skills,
            missing_skills=missing_skills,
            high_priority_skills=high_priority_skills,
            medium_priority_skills=medium_priority_skills,
            low_priority_skills=low_priority_skills,
            match_percentage=match_percentage
        )