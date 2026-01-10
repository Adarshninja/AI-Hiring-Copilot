from sklearn.metrics.pairwise import cosine_similarity
from app.services.embedding import get_embedding


def get_sematic_score(resume_text, jd_text):
    resume_vec = get_embedding(resume_text)
    jd_vec = get_embedding(jd_text)
    
    score = cosine_similarity([resume_vec], [jd_vec])[0][0]
    return float(round(score * 100, 2))

