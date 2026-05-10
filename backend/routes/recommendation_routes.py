"""Recommendation endpoint.

Uses a simple collaborative filtering approach based on user similarity.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from ..database import get_session
from .. import models, schemas
import numpy as np

router = APIRouter()

@router.get("/student/{student_id}", response_model=schemas.RecommendationResponse)
async def recommend(student_id: int, db: AsyncSession = Depends(get_session)):
    # Load all progress data
    result = await db.execute(models.LearningProgress.__table__.select())
    progresses = result.all()
    if not progresses:
        raise HTTPException(status_code=404, detail="No progress data available")

    # Build user-content matrix
    user_ids = sorted(set(p[0] for p in progresses))
    content_ids = sorted(set(p[1] for p in progresses))
    matrix = np.zeros((len(user_ids), len(content_ids)))
    uid_to_idx = {uid: i for i, uid in enumerate(user_ids)}
    cid_to_idx = {cid: j for j, cid in enumerate(content_ids)}
    for p in progresses:
        uid, cid, prog = p[0], p[1], p[2]
        matrix[uid_to_idx[uid], cid_to_idx[cid]] = prog

    # Cosine similarity between target student and others
    target_vec = matrix[uid_to_idx[student_id]]
    if np.all(target_vec == 0):
        # No data for this student – return top difficulty items
        top = await db.execute(models.LearningContent.__table__.select().order_by(models.LearningContent.difficulty.desc()).limit(5))
        contents = top.scalars().all()
        recs = [schemas.Recommendation(content_id=c.id, title=c.title, description=c.description, score=c.difficulty) for c in contents]
        return schemas.RecommendationResponse(recommendations=recs)

    sims = np.dot(matrix, target_vec) / (np.linalg.norm(matrix, axis=1) * np.linalg.norm(target_vec) + 1e-9)
    # Exclude target student
    sims[uid_to_idx[student_id]] = -1
    top_users = np.argsort(sims)[-3:][::-1]

    # Aggregate scores from top users
    scores = np.zeros(len(content_ids))
    for idx in top_users:
        scores += matrix[idx] * sims[idx]
    # Remove already completed items
    scores[target_vec > 0] = -1
    top_indices = np.argsort(scores)[-5:][::-1]
    recs = []
    for idx in top_indices:
        cid = content_ids[idx]
        content = await db.get(models.LearningContent, cid)
        recs.append(schemas.Recommendation(content_id=cid, title=content.title, description=content.description, score=scores[idx]))
    return schemas.RecommendationResponse(recommendations=recs)
