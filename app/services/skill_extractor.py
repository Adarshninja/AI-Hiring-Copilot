import re

SKILLS = [
    "python", "java", "c++",
    "fastapi", "flask", "django",
    "machine learning", "deep learning",
    "numpy", "pandas", "scikit-learn",
    "tensorflow", "pytorch",
    "sql", "mysql", "postgresql",
    "docker", "kubernetes",
    "aws", "gcp", "azure",
    "git", "github",
    "rest api", "microservices",
    "flutter", "esp32", "embedded systems", "iot"   
]


def extract_skills(text: str) -> set:
    text = text.lower()
    found_skills = set()
    
    
    for skills in SKILLS:
        pattern = r"\b" + re.escape(skills) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skills)
            
    return found_skills