"""
Application configuration for EduGenie.
"""

from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()


def as_bool(
    value: str | bool | None,
    default: bool = False
) -> bool:

    if value is None:
        return default

    if isinstance(value, bool):
        return value

    return value.strip().lower() in {
        "1",
        "true",
        "yes",
        "y",
        "on"
    }


@dataclass(frozen=True)
class Settings:

    app_name: str = "EduGenie"

    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")

    gemini_model: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-2.0-flash"
    )

    demo_mode: bool = os.getenv(
        "DEMO_MODE",
        "true"
    ).lower() == "true"


    app_version: str = os.getenv(
        "APP_VERSION",
        "1.0.0"
    )

    host: str = os.getenv(
        "HOST",
        "127.0.0.1"
    )

    port: int = int(
        os.getenv(
            "PORT",
            "8000"
        )
    )

    gemini_api_key: str | None = os.getenv(
        "GEMINI_API_KEY"
    )

    gemini_model: str = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.8-flash"
    )

    local_model_name: str = os.getenv(
        "LOCAL_MODEL_NAME",
        "MBZUAI/LaMini-Flan-T5-783M"
    )

    local_explainer_model: str = os.getenv(
        "LOCAL_EXPLAINER_MODEL",
        "MBZUAI/LaMini-Flan-T5-783M"
    )

    use_local_explainer: bool = (
        os.getenv("USE_LOCAL_EXPLAINER", "false").lower()
        == "true"
    )

    max_input_chars: int = int(
        os.getenv(
            "MAX_INPUT_CHARS",
            "12000"
        )
    )

    max_output_tokens: int = int(
    os.getenv("MAX_OUTPUT_TOKENS", "1000")
)

    local_max_new_tokens: int = int(
        os.getenv(
            "LOCAL_MAX_NEW_TOKENS",
            "180"
        )
    )


settings = Settings()