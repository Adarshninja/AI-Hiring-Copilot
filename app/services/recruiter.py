from app.services.llm import ask_llm

def recruiter_feedback(resume_text, jd_text, semantic_score, matched, missing):
    prompt = f"""
    you are an expert technical recruiter.
    
    Candidate resume:
    {resume_text}
    
    Job description:
    {jd_text}
    
    Match score: {semantic_score}
    
    Matched skills: {matched}
    
    Missing skills: {missing}
    
    
    Give: 
    1. Short explanation of the score
    2. How the candidate should improve
    3. What skills to learn
    4. 3 interview questions based on this job
    """ 
    return ask_llm(prompt)
    