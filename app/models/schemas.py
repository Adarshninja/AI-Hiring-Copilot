from pydantic import BaseModel

class JobDes(BaseModel):
    job_description: str
    
    