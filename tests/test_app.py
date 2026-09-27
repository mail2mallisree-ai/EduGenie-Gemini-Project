import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import main
import gemini_client
from gemini_client import _generate_with_retry
from fastapi.testclient import TestClient
from types import SimpleNamespace


client = TestClient(main.app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_qa_rejects_boolean_text():
    response = client.post("/qa", json={"text": True})
    assert response.status_code == 422


def test_gemini_request_retries_on_service_unavailable(monkeypatch):
    class ServiceUnavailable(Exception):
        status_code = 503

    attempts = 0

    def generate():
        nonlocal attempts
        attempts += 1
        if attempts == 1:
            raise ServiceUnavailable()
        return "ok"

    monkeypatch.setattr("gemini_client.time.sleep", lambda _: None)

    assert _generate_with_retry(generate) == "ok"
    assert attempts == 2


def test_gemini_request_does_not_retry_other_errors(monkeypatch):
    class BadRequest(Exception):
        status_code = 400

    attempts = 0

    def generate():
        nonlocal attempts
        attempts += 1
        raise BadRequest()

    monkeypatch.setattr("gemini_client.time.sleep", lambda _: None)

    try:
        _generate_with_retry(generate)
    except BadRequest:
        pass
    else:
        raise AssertionError("Expected BadRequest to be raised")

    assert attempts == 1


def test_generate_text_uses_chat_send_message(monkeypatch):
    calls = {}

    class Chat:
        def send_message(self, prompt):
            calls["prompt"] = prompt
            return SimpleNamespace(text=" Gemini response ")

    class Chats:
        def create(self, **kwargs):
            calls["config"] = kwargs
            return Chat()

    monkeypatch.setattr(
        gemini_client,
        "get_client",
        lambda: SimpleNamespace(chats=Chats())
    )

    assert gemini_client.generate_text("Test prompt") == "Gemini response"
    assert calls["prompt"] == "Test prompt"