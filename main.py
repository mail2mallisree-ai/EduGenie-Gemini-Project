from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from config import settings
from qna import answer_question
from explanation_module import explain_concept
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import generate_learning_path


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="EduGenie AI",
    description="AI-powered educational assistant"
)


# ==========================
# STATIC FILES
# ==========================

app.mount(
    "/static",
    StaticFiles(
        directory=str(BASE_DIR / "static")
    ),
    name="static"
)


# ==========================
# REQUEST MODEL
# ==========================

class TextRequest(BaseModel):
    text: str


# ==========================
# HOME
# ==========================

@app.get(
    "/",
    response_class=HTMLResponse
)
async def home():

    html_file = BASE_DIR / "templates" / "index.html"

    return html_file.read_text(
        encoding="utf-8"
    )


# ==========================
# HEALTH
# ==========================

@app.get("/health")
async def health():

    return {
        "status": "running",
        "demo_mode": settings.demo_mode
    }


# ==========================
# 1. Q&A
# ==========================

@app.post("/qa")
async def qa(request: TextRequest):

    try:

        result = answer_question(
            request.text
        )

        return {
            "success": True,
            "task": "qa",
            "answer": result,
            "demo_mode": settings.demo_mode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================
# 2. EXPLAIN
# ==========================

@app.post("/explain")
async def explain(request: TextRequest):

    try:

        result = explain_concept(
            request.text
        )

        return {
            "success": True,
            "task": "explain",
            "answer": result,
            "demo_mode": settings.demo_mode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================
# 3. QUIZ
# ==========================

@app.post("/quiz")
async def quiz(request: TextRequest):

    try:

        result = generate_quiz(
            request.text
        )

        return {
            "success": True,
            "task": "quiz",
            "quiz": result,
            "demo_mode": settings.demo_mode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================
# 4. SUMMARIZE
# ==========================

@app.post("/summarize")
async def summarize(request: TextRequest):

    try:

        result = summarize_text(
            request.text
        )

        return {
            "success": True,
            "task": "summarize",
            "summary": result,
            "demo_mode": settings.demo_mode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }


# ==========================
# 5. LEARNING PATH
# ==========================

@app.post("/learn/recommendations")
async def learning_recommendations(
    request: TextRequest
):

    try:

        result = generate_learning_path(
            request.text
        )

        return {
            "success": True,
            "task": "learning_path",
            "recommendations": result,
            "demo_mode": settings.demo_mode
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }