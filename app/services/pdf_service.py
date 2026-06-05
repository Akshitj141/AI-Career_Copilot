from pypdf import PdfReader

from app.utils.text_cleaner import clean_text


class PDFService:

    def extract_text(self, pdf_file):

        reader = PdfReader(pdf_file)

        pages = len(reader.pages)

        extracted_text = []

        for page in reader.pages:
            text = page.extract_text()

            if text:
                extracted_text.append(text)

        full_text = "\n".join(extracted_text)

        full_text = clean_text(full_text)

        return {
            "text": full_text,
            "pages": pages,
            "words": len(full_text.split()),
            "characters": len(full_text),
        }