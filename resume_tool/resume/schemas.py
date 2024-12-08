from pydantic import BaseModel
from typing import List, Optional

class ResumeSchema(BaseModel):
    file_path: str
    skills_extracted: List[str]
    uploaded_at: str
    rating: float
    suggestions: Optional[str] = None

    class Config:
        orm_mode = True 

class ResumeCreateSchema(BaseModel):
    file_path: str

    class Config:
        orm_mode = True
