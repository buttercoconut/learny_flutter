from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from ..models.base import LearningContent
from ..schemas import LearningContentCreate, LearningContentOut

router = APIRouter(prefix="/learning_contents", tags=["learning_contents"])

@router.get("/", response_model=list[LearningContentOut])
async def get_contents(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(LearningContent))
    return [LearningContentOut.from_orm(row) for row in result.scalars().all()]

@router.post("/", response_model=LearningContentOut)
async def add_content(content: LearningContentCreate, session: AsyncSession = Depends(get_session)):
    new_content = LearningContent(title=content.title, content=content.content, difficulty=content.difficulty)
    session.add(new_content)
    await session.commit()
    await session.refresh(new_content)
    return LearningContentOut.from_orm(new_content)
