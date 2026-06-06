from app.models.roadmap_model import (
    LearningRoadmap
)


def test_roadmap_creation():

    roadmap = LearningRoadmap()

    assert roadmap.target_role == ""