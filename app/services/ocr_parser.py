import pytesseract
from PIL import Image
import fitz
import os


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_with_ocr(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    
    for page_number in range(len(doc)):
        page = doc[page_number]
        pix = page.get_pixmap(dpi=300)
        
        image_path = f"temp_page_{page_number}.png"
        pix.save(image_path)
        
        image = Image.open(image_path)
        text += pytesseract.image_to_string(image)
        
        
        os.remove(image_path)
    return text.strip()

# the above code will extract the text's from the scanned pdf also.
        
        