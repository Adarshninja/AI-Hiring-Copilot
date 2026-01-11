import re

SKILLS = [
    # Programming
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "go", "rust",

    # Backend & APIs
    "fastapi", "django", "flask", "spring boot", "node.js", "express",
    "rest api", "graphql", "microservices",

    # AI / ML
    "machine learning", "deep learning", "nlp", "computer vision",
    "pytorch", "tensorflow", "scikit-learn", "xgboost",
    "llm", "rag", "langchain", "prompt engineering",

    # Data
    "numpy", "pandas", "matplotlib", "seaborn",
    "sql", "mysql", "postgresql", "mongodb",
    "power bi", "tableau",

    # Cloud & DevOps
    "docker", "kubernetes", "aws", "gcp", "azure",
    "ci/cd", "github actions",

    # Databases & Search
    "redis", "elasticsearch", "qdrant", "vector database",

    # Frontend
    "react", "next.js", "html", "css", "tailwind",

    # Mobile & IoT
    "flutter", "android", "esp32", "arduino",
    "embedded systems", "iot", "mqtt", "blynk", "thingspeak",

    # Tools
    "git", "github", "linux", "bash", "postman"
]


def extract_skills(text: str) -> set:
    text = text.lower()
    found_skills = set()
    
    
    for skills in SKILLS:
        pattern = r"\b" + re.escape(skills) + r"\b"
        if re.search(pattern, text):
            found_skills.add(skills)
            
    return found_skills

