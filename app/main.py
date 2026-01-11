import os
from fastapi import FastAPI, UploadFile, HTTPException, File, Form
from app.services.pdf_parser import extract_text_from_pdf
from app.services.text_cleaner import clean_text
from app.routes import job
from app.services.skill_extractor import extract_skills
from app.services.matcher import calculate_match_score
from app.services.semantic_matcher import get_sematic_score
from app.services.chunked_semantic import chunked_semantic_score
from app.services.recruiter import recruiter_feedback


app = FastAPI(title="AI - Hiring Copilot")

app.include_router(job.router, tags=["job"])


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type not in ["application/pdf", "text/plain"]:
        raise HTTPException(status_code=400, detail="Only PDF and Text file allowed.")
    
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
        
    
    return {
        "message": "Resume upload successfullt",
        "filename" : file.filename
    }
    
    
@app.post("/match")
async def match_resume_to_job(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
        
    resume_text = clean_text(extract_text_from_pdf(file_path))
    jd_text = clean_text(job_description)
    
    resume_preview = resume_text[:500]
    jd_prev = jd_text[:300]
    
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)
    
    missing_skills = sorted(list(jd_skills - resume_skills))
    matched_skills  = sorted(list(resume_skills & jd_skills))
    
    score = calculate_match_score(resume_text, jd_text)
    semantic_score = chunked_semantic_score(resume_text, jd_text)
    
    ai_feedback = recruiter_feedback(
        resume_text,
        jd_text,
        semantic_score,
        matched_skills,
        missing_skills
    )
    
    return {
        "Rule_based_Score": score,
        "Semantic_based_Score": semantic_score,
        "insides": (
            "Strong match" if semantic_score > 75 else
            "Moderate match" if semantic_score > 50 else
            "Weak match :("
        ),
        "Matched_Skills" : matched_skills,
        "Missing_SKills" : missing_skills,
        "AI-Feedback": ai_feedback,
        "resume_preview": resume_preview,
        "jd_preview": jd_prev
    }
 