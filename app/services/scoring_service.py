from app.models.score_model import (
    ScoreReport
)


class ScoringService:

    def calculate_scores(
        self,
        contact_info,
        sections,
        skills,
        match_percentage=0
    ):

        resume_quality = 0

        if contact_info.email:
            resume_quality += 25

        if contact_info.phone:
            resume_quality += 25

        if contact_info.linkedin:
            resume_quality += 25

        if contact_info.github:
            resume_quality += 25

        skill_score = min(
            len(skills) * 5,
            100
        )

        project_score = (
            100
            if "projects" in sections
            else 50
        )

        experience_score = (
            100
            if "experience" in sections
            else 50
        )

        ats_score = round(
            (
                resume_quality * 0.30
                + skill_score * 0.30
                + project_score * 0.20
                + experience_score * 0.20
            ),
            2
        )

        if match_percentage > 0:

            career_readiness_score = round(
                (
                    ats_score * 0.50
                    + match_percentage * 0.50
                ),
                2
            )

        else:

            career_readiness_score = ats_score

        recommendations = []

        if skill_score < 70:
            recommendations.append(
                "Add more technical skills."
            )

        if project_score < 100:
            recommendations.append(
                "Add project experience."
            )

        if experience_score < 100:
            recommendations.append(
                "Add experience section."
            )

        return ScoreReport(
            ats_score=ats_score,
            job_match_score=match_percentage,
            career_readiness_score=career_readiness_score,
            resume_quality_score=resume_quality,
            skill_score=skill_score,
            project_score=project_score,
            experience_score=experience_score,
            recommendations=recommendations
        )