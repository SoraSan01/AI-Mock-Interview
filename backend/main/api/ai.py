import os
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from openai import OpenAI, OpenAIError
from pydantic import BaseModel, Field

from main.api.auth import get_current_user
from main.models.user import User

router = APIRouter(prefix="/api/ai", tags=["AI"])


class QuestionRequest(BaseModel):
    job_title: str = Field(min_length=2, max_length=100)
    topic: str = Field(min_length=2, max_length=200)
    difficulty: str = Field(default="intermediate", max_length=30)


class QuestionResponse(BaseModel):
    questions: list[str]


@router.post("/questions", response_model=QuestionResponse)
def generate_questions(
    request: QuestionRequest,
    _user: Annotated[User, Depends(get_current_user)],
) -> QuestionResponse:
    try:
        client = OpenAI()
        response = client.responses.parse(
            model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
            input=[
                {
                    "role": "system",
                    "content": (
                        "Write five useful mock interview questions. "
                        "Return concise questions suited to the requested role, "
                        "topic, and difficulty."
                    ),
                },
                {
                    "role": "user",
                    "content": (
                        f"Job title: {request.job_title}\n"
                        f"Topic: {request.topic}\n"
                        f"Difficulty: {request.difficulty}"
                    ),
                },
            ],
            text_format=QuestionResponse,
        )

        if response.output_parsed is None:
            raise HTTPException(status_code=502, detail="AI returned no questions")

        return response.output_parsed
    except OpenAIError:
        raise HTTPException(status_code=502, detail="AI question generation failed") from None