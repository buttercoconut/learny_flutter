from fastapi import FastAPI
from .database import engine, get_session
from .models.base import Base
from .routes.student_routes import router as student_router
from .routes.learning_content_routes import router as content_router

app = FastAPI(title="Learny Backend")

# Include routers
app.include_router(student_router)
app.include_router(content_router)

# Create tables on startup
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency injection for session
app.dependency_overrides[get_session] = get_session
