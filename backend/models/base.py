from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    grade = Column(Integer, nullable=False)
    level = Column(String(20), nullable=False)

class LearningContent(Base):
    __tablename__ = "learning_contents"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    difficulty = Column(String(20), nullable=False)
