import os
import tempfile
import pytest

tmp = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
tmp.close()
os.environ["DATABASE_PATH"] = tmp.name
os.environ["AI_PROVIDER"] = "demo"

from fastapi.testclient import TestClient
from backend.main import app

@pytest.fixture(scope="module")
def client():
    with TestClient(app) as test_client:
        yield test_client

def test_health(client):
    assert client.get("/api/health").json()["status"] == "ok"

def test_chat(client):
    r = client.post("/api/chat", json={"message":"hello", "language":"en"})
    assert r.status_code == 200 and "reply" in r.json()

def test_language_validation(client):
    assert client.post("/api/chat", json={"message":"hello", "language":"fr"}).status_code == 422

def test_emergency_routing(client):
    r = client.post("/api/chat", json={"message":"I have chest pain", "language":"en"})
    assert "medical emergency" in r.json()["reply"]

def test_reminders(client):
    r = client.post("/api/reminders", json={"label":"Test", "time":"13:45"})
    assert r.status_code == 201
    item_id = r.json()["id"]
    assert client.delete(f"/api/reminders/{item_id}").status_code == 200
    assert client.delete(f"/api/reminders/{item_id}").status_code == 404

def test_voice_requires_credentials_in_demo_mode(client):
    r = client.post("/api/voice", json={"text":"سلام", "language":"sd"})
    assert r.status_code == 503

def test_cartoon_avatar_assets(client):
    assert client.get("/assets/ada-avatar.svg").status_code == 200
    assert client.get("/assets/adi-avatar.svg").status_code == 200
