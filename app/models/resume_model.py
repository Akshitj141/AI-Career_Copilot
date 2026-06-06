from dataclasses import dataclass, field


@dataclass
class ContactInfo:
    name: str = ""
    email: str = ""
    phone: str = ""
    linkedin: str = ""
    github: str = ""


@dataclass
class Education:
    degree: str = ""
    institution: str = ""
    year: str = ""


@dataclass
class Experience:
    title: str = ""
    company: str = ""
    duration: str = ""
    description: str = ""


@dataclass
class Project:
    name: str = ""
    description: str = ""
    technologies: list[str] = field(default_factory=list)


@dataclass
class ResumeData:
    contact: ContactInfo = field(default_factory=ContactInfo)

    skills: list[str] = field(default_factory=list)

    education: list[Education] = field(default_factory=list)

    experience: list[Experience] = field(default_factory=list)

    projects: list[Project] = field(default_factory=list)

    certifications: list[str] = field(default_factory=list)

    achievements: list[str] = field(default_factory=list)