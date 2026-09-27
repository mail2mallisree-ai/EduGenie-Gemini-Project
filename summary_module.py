from gemini_client import generate_text
from config import settings


def summarize_text(text: str) -> str:

    if settings.demo_mode:

        words = text.split()

        if len(words) <= 40:
            return (
                "Summary: " + text
            )

        short_text = " ".join(words[:40])

        return (
            "Demo Summary:\n"
            + short_text
            + "..."
        )

    prompt = f"""
Summarize the following text for a college student.

Text:
{text}

Requirements:
- Keep it concise
- Use simple English
- Preserve the important points
"""

    return generate_text(prompt)