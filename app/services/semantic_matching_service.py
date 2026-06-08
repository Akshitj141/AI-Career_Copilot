from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from app.models.semantic_match_model import (
    SemanticMatchReport
)


class SemanticMatchingService:

    def __init__(self):

        self.model = (
            SentenceTransformer(
                "all-MiniLM-L6-v2"
            )
        )

    def calculate_similarity(
        self,
        resume_text: str,
        jd_text: str,
        keyword_score: float
    ) -> SemanticMatchReport:

        if not jd_text.strip():

            return SemanticMatchReport()

        resume_embedding = (
            self.model.encode(
                resume_text
            )
        )

        jd_embedding = (
            self.model.encode(
                jd_text
            )
        )

        semantic_score = round(
            cosine_similarity(
                [resume_embedding],
                [jd_embedding]
            )[0][0]
            * 100,
            2
        )

        overall_score = round(
            (
                keyword_score * 0.4
                +
                semantic_score * 0.6
            ),
            2
        )

        return SemanticMatchReport(
            semantic_match_score=semantic_score,
            overall_match_score=overall_score
        )