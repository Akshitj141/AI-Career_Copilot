import re

from app.utils.regex_patterns import EMAIL_PATTERN


def test_email_pattern():
    text = "Contact me at test@gmail.com"

    emails = re.findall(EMAIL_PATTERN, text)

    assert emails[0] == "test@gmail.com"