import streamlit as st

from app.services.pdf_service import PDFService


st.title("AI Resume Intelligence Platform")

uploaded_file = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

if uploaded_file:

    pdf_service = PDFService()

    result = pdf_service.extract_text(uploaded_file)

    st.success("Resume Uploaded")

    st.write("Pages:", result["pages"])
    st.write("Words:", result["words"])

    st.text_area(
        "Extracted Text",
        result["text"],
        height=300
    )