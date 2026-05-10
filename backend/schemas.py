"""Pydantic schemas for API payloads.
"""

from pydantic import BaseModel, Field
from typing import List, Optional
import datetime

# Student schemas
class StudentBase(BaseModel):
    name: str = Field(..., max_length=100)
    grade: int
    level: float = Field(..., ge=0.0, le=1.0)

class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int

    class Config:
        orm_mode = True

# LearningContent schemas
class ContentBase(BaseModel):
    title: str
    description: Optional[str] = None
    difficulty: float = Field(..., ge=0.0, le=5.0)
    tags: Optional[List[str]] = None

class ContentCreate(ContentBase):
    pass

class ContentRead(ContentBase):
    id: int

    class Config:
        orm_mode = True

# LearningPlan schemas
class PlanBase(BaseModel):
    student_id: int
    content_id: int
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None

class PlanCreate(PlanBase):
    pass

class PlanRead(PlanBase):
    id: int

    class Config:
        orm_mode = True

# LearningProgress schemas
class ProgressBase(BaseModel):
    student_id: int
    content_id: int
    progress: float = Field(..., ge=0.0, le=1.0)

class ProgressCreate(ProgressBase):
    pass

class ProgressRead(ProgressBase):
    id: int
    last_updated: datetime.datetime

    class Config:
        orm_mode = True

# Recommendation response
class Recommendation(BaseModel):
    content_id: int
    title: str
    description: Optional[str]
    score: float

class RecommendationResponse(BaseModel):
    recommendations: List[Recommendation]

