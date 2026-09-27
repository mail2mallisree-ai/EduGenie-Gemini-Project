from gemini_client import generate_text
from config import settings


def generate_learning_path(topic: str):

    if settings.demo_mode:

        return {
            "topic": topic,
            "level": "Beginner to Advanced",
            "estimated_duration": "4 weeks",
            "steps": [
                {
                    "week": 1,
                    "title": f"Introduction to {topic}",
                    "difficulty": "Beginner",
                    "description": f"Learn the basic concepts of {topic}.",
                    "resources": [
                        "Basic notes",
                        "Beginner tutorials"
                    ]
                },
                {
                    "week": 2,
                    "title": f"Core Concepts of {topic}",
                    "difficulty": "Beginner",
                    "description": f"Understand the important concepts of {topic}.",
                    "resources": [
                        "Examples",
                        "Practice exercises"
                    ]
                },
                {
                    "week": 3,
                    "title": f"Practical {topic}",
                    "difficulty": "Intermediate",
                    "description": f"Practice {topic} using real examples.",
                    "resources": [
                        "Mini projects",
                        "Coding exercises"
                    ]
                },
                {
                    "week": 4,
                    "title": f"Advanced {topic}",
                    "difficulty": "Advanced",
                    "description": f"Explore advanced applications of {topic}.",
                    "resources": [
                        "Advanced tutorials",
                        "Project work"
                    ]
                }
            ]
        }

    prompt = f"""
Create a personalized learning path for:

{topic}

Include:
- Beginner topics
- Intermediate topics
- Advanced topics
- Difficulty level
- Resources
- Suggested timeline
"""

    result = generate_text(prompt)

    return {
        "topic": topic,
        "learning_path": result
    }