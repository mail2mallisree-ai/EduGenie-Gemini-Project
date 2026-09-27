from gemini_client import generate_text
from config import settings


def answer_question(question: str) -> str:

    if settings.demo_mode:

        return (
            "Photosynthesis is the process by which green plants "
            "use sunlight, carbon dioxide, and water to make glucose "
            "and release oxygen."
        )

    prompt = f"""
You are EduGenie, an educational AI assistant.

Answer the following question clearly for a beginner.

Question:
{question}

Give a simple and accurate explanation.
"""

    return generate_text(prompt)