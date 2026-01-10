from app.services.embedding import get_embedding
from app.services.chunker import chunk_text
from sklearn.metrics.pairwise import cosine_similarity


def chunked_semantic_score(resume_text, jd_text):
    resume_chunks = chunk_text(resume_text)
    jd_chunks = chunk_text(jd_text)
    
    resume_vectors = [get_embedding(c) for c in resume_chunks]
    jd_vectors = [get_embedding(c) for c in jd_chunks]
    
    best_scores = []
    
    for i in resume_vectors:
        similarity = cosine_similarity([i], jd_vectors)[0]
        best_scores.append(max(similarity))
        
        
    final_score = sum(best_scores) / len(best_scores)
    
    return float(round(final_score * 100, 2))

