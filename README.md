# EduGenie - AI Learning Assistant

EduGenie is an AI-powered educational assistant built with:

- FastAPI
- Google Gemini
- LaMini-Flan-T5
- HTML
- CSS
- JavaScript

## Features

1. Question Answering
2. Concept Explanation
3. Quiz Generation
4. Text Summarization
5. Learning Path Recommendation

## Project Structure

EduGenie/

├── main.py
├── config.py
├── schemas.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── run.bat
├── run.sh
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── app.js
│
└── tests/
    ├── conftest.py
    └── test_app.py

## Installation

Create a virtual environment.

### Windows

python -m venv .venv

Activate it:

.venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

## Gemini API

Create a Google Gemini API key.

Open `.env`.

Add:

GEMINI_API_KEY=YOUR_REAL_KEY

GEMINI_MODEL=gemini-3.8-flash

## Run

uvicorn main:app --reload

Open:

http://127.0.0.1:8000

## API Documentation

http://127.0.0.1:8000/docs

## Health Check

http://127.0.0.1:8000/health

## API Endpoints

POST /qa

POST /explain

POST /quiz

POST /summarize

POST /learn/recommendations

## Testing

Run:

pytest -q

## Local Explanation Model

The application attempts to use:

MBZUAI/LaMini-Flan-T5-783M

for concept explanations when:

USE_LOCAL_EXPLAINER=true

To use Gemini instead:

USE_LOCAL_EXPLAINER=false

## Common Problems

### GEMINI_API_KEY error

Check `.env`.

### ModuleNotFoundError

Run:

pip install -r requirements.txt

### Port error

Run:

uvicorn main:app --reload --port 8001

Then open:

http://127.0.0.1:8001

### Local model problem

Set:

USE_LOCAL_EXPLAINER=false

This makes the explanation feature use Gemini.
