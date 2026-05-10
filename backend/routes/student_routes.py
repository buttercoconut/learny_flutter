from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.base import Student
from ..schemas import StudentCreate, StudentOut

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/", response_model=list[StudentOut])
async def get_students(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Student))
    return [StudentOut.from_orm(row) for row in result.scalars().all()]

@router.post("/", response_model=StudentOut)
async def add_student(student: StudentCreate, session: AsyncSession = Depends(get_session)):
    new_student = Student(name=student.name, grade=student.grade, level=student.level)
    session.add(new_student)
    await session.commit()
    await session.refresh(new_student)
    return StudentOut.from_orm(new_student)
