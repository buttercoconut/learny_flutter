from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic import BaseModel
from typing import List

# Database setup
DATABASE_URL = "sqlite+aiosqlite:///./learny.db"
engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()

# Pydantic schemas
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

# FastAPI app
app = FastAPI(title="Learny Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# Routes
@app.get("/students", response_model=List[StudentOut])
async def read_students(session: AsyncSession = Depends(get_session)):
    result = await session.execute("SELECT * FROM students")
    return [StudentOut.from_orm(row) for row in result.fetchall()]

@app.post("/students", response_model=StudentOut)
async def create_student(student: StudentCreate, session: AsyncSession = Depends(get_session)):
    new_student = Student(name=student.name, grade=student.grade, level=student.level)
    session.add(new_student)
    await session.commit()
    await session.refresh(new_student)
    return StudentOut.from_orm(new_student)

@app.get("/learning_contents", response_model=List[LearningContentOut])
async def read_contents(session: AsyncSession = Depends(get_session)):
    result = await session.execute("SELECT * FROM learning_contents")
    return [LearningContentOut.from_orm(row) for row in result.fetchall()]

@app.post("/learning_contents", response_model=LearningContentOut)
async def create_content(content: LearningContentCreate, session: AsyncSession = Depends(get_session)):
    new_content = LearningContent(title=content.title, content=content.content, difficulty=content.difficulty)
    session.add(new_content)
    await session.commit()
    await session.refresh(new_content)
    return LearningContentOut.from_orm(new_content)

@app.get("/recommend/{student_id}")
async def recommend(student_id: int, session: AsyncSession = Depends(get_session)):
    # Simple recommendation: return top 5 contents sorted by difficulty
    result = await session.execute("SELECT * FROM learning_contents ORDER BY difficulty LIMIT 5")
    return [LearningContentOut.from_orm(row) for row in result.fetchall()]
