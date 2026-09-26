import os
from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

from main.api.auth import router as auth_router
from main.api.ai import router as ai_router
from main.db.database import Base, engine
from main.models.user import User  # noqa: F401 - registers the model with SQLAlchemy metadata


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="AI Mock Interview API",
    version="1.0.0",
    lifespan=lifespan,
)

frontend_url = os.getenv("FRONTEND_URL", "http://localhost:5173").rstrip("/")
app.add_middleware(
    CORSMiddleware,
    allow_origins=list({frontend_url, "http://localhost:5173", "http://127.0.0.1:5173"}),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(ai_router)

@app.get("/", tags=["Health"])
def root() -> dict[str, str]:
    return {"message": "AI Mock Interview API is running"}

@app.get("/api/health", tags=["Health"])
def health() -> dict[str, str]:
    return {"status": "ok"}
