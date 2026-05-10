"""FastAPI application entry point.

This file sets up the FastAPI app, includes routers, and provides a simple
health‑check endpoint.  The database connection is configured via SQLAlchemy
with async support for PostgreSQL.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from .routes.student_routes import router as student_router
from .routes.learning_content_routes import router as content_router
from .routes.recommendation_routes import router as recommend_router

# Create FastAPI app
app = FastAPI(title="Learny Backend", description="Backend for Learny Flutter app", version="0.1.0")

# Allow CORS for local dev (Flutter app runs on http://localhost:3000 or similar)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production restrict this
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(content_router, prefix="/contents", tags=["learning_contents"])
app.include_router(recommend_router, prefix="/recommend", tags=["recommendation"])

@app.get("/health", tags=["health"])
async def health_check():
    return {"status": "ok"}

# Run with: uvicorn backend.main:app --reload
