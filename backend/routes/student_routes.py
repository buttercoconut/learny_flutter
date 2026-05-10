"""Student CRUD router.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ..database import get_session
from .. import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.StudentRead, status_code=status.HTTP_201_CREATED)
async def create_student(student: schemas.StudentCreate, db: AsyncSession = Depends(get_session)):
    new_student = models.Student(**student.dict())
    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)
    return new_student

@router.get("/", response_model=List[schemas.StudentRead])
async def list_students(db: AsyncSession = Depends(get_session)):
    result = await db.execute(models.Student.__table__.select())
    students = result.scalars().all()
    return students

@router.get("/{student_id}", response_model=schemas.StudentRead)
async def get_student(student_id: int, db: AsyncSession = Depends(get_session)):
    student = await db.get(models.Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.put("/{student_id}", response_model=schemas.StudentRead)
async def update_student(student_id: int, student_in: schemas.StudentCreate, db: AsyncSession = Depends(get_session)):
    student = await db.get(models.Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    for key, value in student_in.dict().items():
        setattr(student, key, value)
    await db.commit()
    await db.refresh(student)
    return student

@router.delete("/{student_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_student(student_id: int, db: AsyncSession = Depends(get_session)):
    student = await db.get(models.Student, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    await db.delete(student)
    await db.commit()
    return None
