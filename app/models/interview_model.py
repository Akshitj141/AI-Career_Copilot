from dataclasses import dataclass, field


@dataclass
class InterviewQuestionSet:

    technical_questions: list[str] = field(
        default_factory=list
    )

    behavioral_questions: list[str] = field(
        default_factory=list
    )

    resume_based_questions: list[str] = field(
        default_factory=list
    )

    project_based_questions: list[str] = field(
        default_factory=list
    )