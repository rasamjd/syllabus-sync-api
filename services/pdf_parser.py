import pdfplumber
import io

# To decode to string text

def pdf_bytes_to_text(pdf_bytes: bytes) -> str:
  
  text = ""
  with pdfplumber.open(io.BytesIO(pdf_bytes)) as pdf:
    for page in pdf.pages:
      text += page.extract_text() or ""
  return text