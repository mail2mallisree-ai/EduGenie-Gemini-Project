"""
Pydantic schemas used by the EduGenie API.
"""

from pydantic import BaseModel, Field, field_validator


class TextRequest(BaseModel):

    text: str = Field(
        ...,
        min_length=1,
        max_length=12000
    )

    @field_validator("text", mode="before")
    @classmethod
    def validate_text(
        cls,
        value: object
    ) -> str:

        if not isinstance(value, str):
            raise ValueError(
                "Input text must be a string."
            )

        value = value.strip()

        if not value:
            raise ValueError(
                "Input text cannot be empty."
            )

        return value


class TextResponse(BaseModel):

    result: str


class QuizQuestion(BaseModel):

    question: str

    options: list[str] = Field(
        min_length=4,
        max_length=4
    )

    correct_answer: int = Field(
        ge=0,
        le=3
    )

    explanation: str


class QuizResponse(BaseModel):

    questions: list[QuizQuestion] = Field(
        min_length=3,
        max_length=3
    )