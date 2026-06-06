from dataclasses import dataclass, field


@dataclass
class LearningRoadmap:

    target_role: str = ""

    thirty_day_plan: list[str] = field(
        default_factory=list
    )

    sixty_day_plan: list[str] = field(
        default_factory=list
    )

    ninety_day_plan: list[str] = field(
        default_factory=list
    )