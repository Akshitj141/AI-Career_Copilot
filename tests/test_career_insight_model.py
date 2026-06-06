from app.models.career_insight_model import (
    CareerInsight
)


def test_career_insight_creation():

    insight = CareerInsight()

    assert insight.strengths == []