from app.services.pdf_service import PDFService


def test_service_creation():

    service = PDFService()

    assert service is not None