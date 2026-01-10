import re

def clean_text(text: str) -> str:
    text = re.sub(r'\n+', '\n', text)
    
    text = re.sub(r'\s+', ' ', text)
    
    text = re.sub(f'[^\x00-\x7F]+', ' ', text)
    
    
    return text.strip()

