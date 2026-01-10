from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_match_score(resume_text : str, jd_text: str) -> float:
    vector = TfidfVectorizer(stop_words="english")
    vectors = vector.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    
    return round(float(similarity[0][0]) * 100, 2)

