"""ORM models for Learny.

Defines Student, LearningContent, LearningPlan, LearningProgress.
"""

from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from .database import Base
import datetime

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    grade = Column(Integer, nullable=False)  # 학년
    level = Column(Float, nullable=False, default=0.0)  # 학습 수준(0.0~1.0)

    plans = relationship("LearningPlan", back_populates="student")
    progresses = relationship("LearningProgress", back_populates="student")

class LearningContent(Base):
    __tablename__ = "learning_contents"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    difficulty = Column(Float, nullable=False, default=1.0)
    tags = Column(Text, nullable=True)  # comma separated tags for content‑based filtering

    progresses = relationship("LearningProgress", back_populates="content")

class LearningPlan(Base):
    __tablename__ = "learning_plans"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    content_id = Column(Integer, ForeignKey("learning_contents.id"), nullable=False)
    start_date = Column(DateTime, default=datetime.datetime.utcnow)
    end_date = Column(DateTime, nullable=True)

    student = relationship("Student", back_populates="plans")
    content = relationship("LearningContent")

class LearningProgress(Base):
    __tablename__ = "learning_progress"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)
    content_id = Column(Integer, ForeignKey("learning_contents.id"), nullable=False)
    progress = Column(Float, default=0.0)  # 0.0~1.0
    last_updated = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    student = relationship("Student", back_populates="progresses")
    content = relationship("LearningContent", back_populates="progresses")

# Back‑populates
Student.plans = relationship("LearningPlan", back_populates="student", cascade="all, delete-orphan")
Student.progresses = relationship("LearningProgress", back_populates="student", cascade="all, delete-orphan")
LearningContent.progresses = relationship("LearningProgress", back_populates="content", cascade="all, delete-orphan")
