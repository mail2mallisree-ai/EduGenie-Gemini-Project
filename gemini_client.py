from google import genai
from google.genai import types
from config import settings


def get_client():

    if not settings.gemini_api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is missing in .env"
        )

    return genai.Client(
        api_key=settings.gemini_api_key
    )


def generate_text(
    prompt: str,
    max_output_tokens: int = None,
    temperature: float = None
) -> str:

    # DEMO MODE
    if settings.demo_mode:
        return "DEMO_MODE_ACTIVE"

    client = get_client()

    output_tokens = (
        max_output_tokens
        if max_output_tokens is not None
        else settings.max_output_tokens
    )

    config = types.GenerateContentConfig(
        max_output_tokens=output_tokens
    )

    try:

        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
            config=config
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text.strip()

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:
            raise RuntimeError(
                "Gemini API rate limit reached."
            )

        if "503" in error_message:
            raise RuntimeError(
                "Gemini service is temporarily unavailable."
            )

        raise RuntimeError(
            f"Gemini API error: {error_message}"
        )


def generate_structured(
    prompt: str,
    response_schema,
    max_output_tokens: int = None,
    temperature: float = None
):

    # DEMO MODE
    if settings.demo_mode:
        return None

    client = get_client()

    output_tokens = (
        max_output_tokens
        if max_output_tokens is not None
        else settings.max_output_tokens
    )

    config = types.GenerateContentConfig(
        max_output_tokens=output_tokens,
        response_mime_type="application/json",
        response_schema=response_schema
    )

    try:

        response = client.models.generate_content(
            model=settings.gemini_model,
            contents=prompt,
            config=config
        )

        if not response.text:
            raise RuntimeError(
                "Gemini returned an empty response."
            )

        return response.text.strip()

    except Exception as e:

        error_message = str(e)

        if "429" in error_message:
            raise RuntimeError(
                "Gemini API rate limit reached."
            )

        if "503" in error_message:
            raise RuntimeError(
                "Gemini service is temporarily unavailable."
            )

        raise RuntimeError(
            f"Gemini API error: {error_message}"
        )