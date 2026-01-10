import fitz
from app.services.ocr_parser import extract_text_with_ocr

def extract_text_from_pdf(pdf_path : str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    
    for page in doc:
        text += page.get_text("text") + "\n"
        
    if not text.strip():
        text = extract_text_with_ocr(pdf_path)
        
    return text.strip()

# if it fail to extract text from pdf in case of scanned pdf, use ocr for
# text extraction because that uses more advanced technique to extract text
# even from image.