import pytest
from app import create_app, db
from app.models import Applicant

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.app_context():
        db.drop_all()
        db.create_all()
    with app.test_client() as client:
        yield client
    with app.app_context():
        db.session.remove()
        db.drop_all()

def test_add_applicant(client):
    response = client.post("/api/add", data={
        "name": "Alice",
        "email": "alice@test.com",
        "score": "90"
    })
    assert response.status_code == 200

def test_top_applicants(client):
    # Add sample
    client.post("/api/add", data={"name":"Bob","email":"bob@test.com","score":"85"})
    client.post("/api/add", data={"name":"Charlie","email":"charlie@test.com","score":"75"})
    resp = client.get("/api/applicants/top")
    data = resp.get_json()
    assert len(data) == 1
    assert data[0]["name"] == "Bob"
