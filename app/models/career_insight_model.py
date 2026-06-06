from dataclasses import dataclass, field


@dataclass
class CareerInsight:

    strengths: list[str] = field(
        default_factory=list
    )

    weaknesses: list[str] = field(
        default_factory=list
    )

    recommendations: list[str] = field(
        default_factory=list
    )