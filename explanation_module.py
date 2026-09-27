from gemini_client import generate_text
from config import settings


def explain_concept(topic: str) -> str:

    if settings.demo_mode:

        return f"""
{topic} - Simple Explanation

{topic} is an important concept that can be understood
by learning its basic definition, purpose, and examples.

Example:
Suppose we are learning {topic}. We first understand
what it means, then how it works, and finally where
it is used in real life.

Key Point:
Learn the basic idea first and then move to advanced concepts.
"""

    prompt = f"""
Explain the following concept to a beginner:

{topic}

Use:
1. Simple definition
2. Easy explanation
3. Example
4. Key point
"""

    return generate_text(prompt)