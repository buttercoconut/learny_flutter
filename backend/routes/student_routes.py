"""Student API routes."""

from fastapi import APIRouter, HTTPException, status
from typing import List

from models.student import Student, StudentCreate
from database import add_student, get_student, list_students

router = APIRouter()

@router.post("/", response_model=Student, status_code=status.HTTP_201_CREATED)
async def create_student(student_in: StudentCreate):
    return add_student(student_in)

@router.get("/", response_model=List[Student])
async def read_students():
    return list_students()

@router.get("/{student_id}", response_model=Student)
async def read_student(student_id: int):
    student = get_student(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student
