EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

PHONE_PATTERN = (
    r"(?:\+91[\-\s]?)?"
    r"(?:\d{10})"
)

LINKEDIN_PATTERN = (
    r"(https?:\/\/)?(www\.)?"
    r"linkedin\.com\/in\/[A-Za-z0-9_-]+"
)

GITHUB_PATTERN = (
    r"(https?:\/\/)?(www\.)?"
    r"github\.com\/[A-Za-z0-9_-]+"
)