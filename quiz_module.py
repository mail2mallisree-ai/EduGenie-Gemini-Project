import json
from gemini_client import generate_structured
from config import settings


def generate_quiz(topic: str):

    # ==========================
    # DEMO MODE
    # ==========================

    if settings.demo_mode:

        return {
            "topic": topic,
            "questions": [
                {
                    "question": f"What is the main purpose of learning {topic}?",
                    "options": [
                        "To understand the concept",
                        "To avoid studying",
                        "To remove all examples",
                        "To skip practice"
                    ],
                    "answer": "To understand the concept"
                },
                {
                    "question": f"Which approach is useful when studying {topic}?",
                    "options": [
                        "Learn basics first",
                        "Skip fundamentals",
                        "Avoid practice",
                        "Memorize without understanding"
                    ],
                    "answer": "Learn basics first"
                },
                {
                    "question": f"What helps improve knowledge of {topic}?",
                    "options": [
                        "Practice and examples",
                        "Ignoring mistakes",
                        "Avoiding questions",
                        "Skipping revision"
                    ],
                    "answer": "Practice and examples"
                }
            ]
        }

    # ==========================
    # GEMINI MODE
    # ==========================

    prompt = f"""
Create exactly 3 multiple-choice questions about:

{topic}

Each question must have:
- One question
- Exactly 4 options
- One correct answer

Return JSON only.
"""

    schema = {
        "type": "object",
        "properties": {
            "topic": {
                "type": "string"
            },
            "questions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "question": {
                            "type": "string"
                        },
                        "options": {
                            "type": "array",
                            "items": {
                                "type": "string"
                            }
                        },
                        "answer": {
                            "type": "string"
                        }
                    },
                    "required": [
                        "question",
                        "options",
                        "answer"
                    ]
                }
            }
        },
        "required": [
            "topic",
            "questions"
        ]
    }

    result = generate_structured(
        prompt,
        schema
    )

    if not result:
        raise RuntimeError(
            "Unable to generate quiz."
        )

    return json.loads(result)