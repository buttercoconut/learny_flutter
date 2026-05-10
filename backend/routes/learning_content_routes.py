"""Learning content CRUD router.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ..database import get_session
from .. import models, schemas

router = APIRouter()

@router.post("/", response_model=schemas.ContentRead, status_code=status.HTTP_201_CREATED)
async def create_content(content: schemas.ContentCreate, db: AsyncSession = Depends(get_session)):
    new_content = models.LearningContent(**content.dict())
    db.add(new_content)
    await db.commit()
    await db.refresh(new_content)
    return new_content

@router.get("/", response_model=List[schemas.ContentRead])
async def list_contents(db: AsyncSession = Depends(get_session)):
    result = await db.execute(models.LearningContent.__table__.select())
    contents = result.scalars().all()
    return contents

@router.get("/{content_id}", response_model=schemas.ContentRead)
async def get_content(content_id: int, db: AsyncSession = Depends(get_session)):
    content = await db.get(models.LearningContent, content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.put("/{content_id}", response_model=schemas.ContentRead)
async def update_content(content_id: int, content_in: schemas.ContentCreate, db: AsyncSession = Depends(get_session)):
    content = await db.get(models.LearningContent, content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    for key, value in content_in.dict().items():
        setattr(content, key, value)
    await db.commit()
    await db.refresh(content)
    return content

@router.delete("/{content_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_content(content_id: int, db: AsyncSession = Depends(get_session)):
    content = await db.get(models.LearningContent, content_id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    await db.delete(content)
    await db.commit()
    return None
