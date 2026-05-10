from pydantic import BaseModel

class StudentCreate(BaseModel):
    name: str
    grade: int
    level: str

class StudentOut(BaseModel):
    id: int
    name: str
    grade: int
    level: str

    class Config:
        orm_mode = True

class LearningContentCreate(BaseModel):
    title: str
    content: str
    difficulty: str

class LearningContentOut(BaseModel):
    id: int
    title: str
    content: str
    difficulty: str

    class Config:
        orm_mode = True
