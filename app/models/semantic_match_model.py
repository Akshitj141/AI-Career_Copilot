from dataclasses import dataclass


@dataclass
class SemanticMatchReport:

    semantic_match_score: float = 0.0

    overall_match_score: float = 0.0