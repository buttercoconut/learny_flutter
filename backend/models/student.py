"""Pydantic models for Student and LearningContent."""

from pydantic import BaseModel, Field
from typing import Optional

class StudentBase(BaseModel):
    name: str = Field(..., example="민준")
    grade: int = Field(..., ge=1, le=6, example=3)
    level: str = Field(..., example="초급")

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True

class LearningContentBase(BaseModel):
    title: str = Field(..., example="수학 기초")
    content: str = Field(..., example="이것은 수학 기초 내용입니다.")
    difficulty: str = Field(..., example="초급")

class LearningContentCreate(LearningContentBase):
    pass

class LearningContent(LearningContentBase):
    id: int

    class Config:
        orm_mode = True
