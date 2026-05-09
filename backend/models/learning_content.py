"""Pydantic models for LearningContent."""

from pydantic import BaseModel, Field

class LearningContentBase(BaseModel):
    title: str = Field(..., example="과학 탐험")
    content: str = Field(..., example="과학 탐험 내용입니다.")
    difficulty: str = Field(..., example="중급")

class LearningContentCreate(LearningContentBase):
    pass

class LearningContent(LearningContentBase):
    id: int

    class Config:
        orm_mode = True
