"""In-memory data store for demo purposes."""

from typing import Dict, List
from models.student import Student, StudentCreate
from models.learning_content import LearningContent, LearningContentCreate

# Simple auto-increment ID counters
_student_id_seq = 1
_content_id_seq = 1

# In-memory storage
students: Dict[int, Student] = {}
contents: Dict[int, LearningContent] = {}

# Helper functions

def add_student(student_in: StudentCreate) -> Student:
    global _student_id_seq
    student = Student(id=_student_id_seq, **student_in.dict())
    students[_student_id_seq] = student
    _student_id_seq += 1
    return student

def get_student(student_id: int) -> Student | None:
    return students.get(student_id)

def list_students() -> List[Student]:
    return list(students.values())

# Learning content helpers

def add_content(content_in: LearningContentCreate) -> LearningContent:
    global _content_id_seq
    content = LearningContent(id=_content_id_seq, **content_in.dict())
    contents[_content_id_seq] = content
    _content_id_seq += 1
    return content

def get_content(content_id: int) -> LearningContent | None:
    return contents.get(content_id)

def list_contents() -> List[LearningContent]:
    return list(contents.values())

# Seed some data for demo
if not contents:
    add_content(LearningContentCreate(title="수학 기초", content="수학 기초 내용", difficulty="초급"))
    add_content(LearningContentCreate(title="과학 탐험", content="과학 탐험 내용", difficulty="중급"))

if not students:
    add_student(StudentCreate(name="민준", grade=3, level="초급"))
    add_student(StudentCreate(name="지은", grade=4, level="중급"))
