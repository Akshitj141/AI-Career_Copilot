from app.services.parser_service import ParserService


def test_contact_info_extraction():

    sample_text = """
    John Doe
    john@gmail.com
    +91 9876543210
    https://linkedin.com/in/johndoe
    https://github.com/johndoe
    """

    parser = ParserService()

    contact = parser.extract_contact_info(sample_text)

    assert contact.email == "john@gmail.com"
    assert "9876543210" in contact.phone
    assert "linkedin.com" in contact.linkedin
    assert "github.com" in contact.github