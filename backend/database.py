"""Database configuration and session management.

Uses SQLAlchemy 2.0 async API with asyncpg driver.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost:5432/learny")

engine = create_async_engine(DATABASE_URL, echo=False, future=True)

# Session local for dependency injection
async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)

Base = declarative_base()

# Dependency
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session

# Create tables helper
async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Call init_models() during startup event if needed
