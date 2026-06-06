import re

from app.models.resume_model import ContactInfo
from app.utils.regex_patterns import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    LINKEDIN_PATTERN,
    GITHUB_PATTERN
)


class ParserService:

    def extract_contact_info(self, text: str) -> ContactInfo:

        email_match = re.search(EMAIL_PATTERN, text)

        phone_match = re.search(PHONE_PATTERN, text)

        linkedin_match = re.search(LINKEDIN_PATTERN, text)

        github_match = re.search(GITHUB_PATTERN, text)

        return ContactInfo(
            email=email_match.group(0) if email_match else "",
            phone=phone_match.group(0) if phone_match else "",
            linkedin=linkedin_match.group(0) if linkedin_match else "",
            github=github_match.group(0) if github_match else "",
        )