"""FastAPI application entry point for learny backend."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from routes.student_routes import router as student_router
from routes.learning_content_routes import router as content_router

app = FastAPI(title="Learny Backend API", version="0.1.0")

# Allow CORS for Flutter app (localhost:3000 or mobile)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(student_router, prefix="/students", tags=["students"])
app.include_router(content_router, prefix="/contents", tags=["learning_contents"])

@app.get("/")
async def root():
    return {"message": "Welcome to Learny Backend API"}
