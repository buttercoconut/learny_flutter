"""Learning content API routes."""

from fastapi import APIRouter, HTTPException, status
from typing import List

from models.learning_content import LearningContent, LearningContentCreate
from database import add_content, get_content, list_contents

router = APIRouter()

@router.post("/", response_model=LearningContent, status_code=status.HTTP_201_CREATED)
async def create_content(content_in: LearningContentCreate):
    return add_content(content_in)

@router.get("/", response_model=List[LearningContent])
async def read_contents():
    return list_contents()

@router.get("/{content_id}", response_model=LearningContent)
async def read_content(content_id: int):
    content = get_content(content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content
