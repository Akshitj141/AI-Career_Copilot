from app.services.parser_service import ParserService


def test_section_detection():

    text = """
    EDUCATION

    B.Tech

    SKILLS

    Python SQL
    """

    parser = ParserService()

    sections = parser.identify_sections(text)

    assert sections["education"] is True
    assert sections["skills"] is True