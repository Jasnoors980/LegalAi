import os
from PyPDF2 import PdfReader
from docx import Document

def get_text(file_path):
    filename = os.path.basename(file_path).lower()

    if filename.endswith('.pdf'):
        try:
            reader = PdfReader(file_path)
            text = " ".join(
                page.extract_text() or "" for page in reader.pages
            )
            if not text.strip():
                raise ValueError("No extractable text found in PDF.")
            return text
        except Exception as e:
            raise ValueError(f"PDF processing failed: {str(e)}")

    elif filename.endswith('.docx'):
        try:
            doc = Document(file_path)
            return "\n".join([para.text for para in doc.paragraphs if para.text.strip()])
        except Exception as e:
            raise ValueError(f"DOCX processing failed: {str(e)}")

    elif filename.endswith('.txt'):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            raise ValueError(f"TXT file reading failed: {str(e)}")

    else:
        raise ValueError("Unsupported file format. Please upload PDF, DOCX, or TXT.")
