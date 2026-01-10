from fastapi import APIRouter
from app.models.schemas import JobDes

router = APIRouter()

@router.post("/job-description")
def submit_job_description(payload: JobDes):
    return{
        "message" : "Job Description received",
        "length" : len(payload.job_description)
    }
    
    