from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    response = client.post(f"/activities/{activity_name}/signup?email={email}")
    assert response.status_code == 200, response.text

    response = client.delete(f"/activities/{activity_name}/unregister?email={email}")
    assert response.status_code == 200, response.text

    activities = client.get("/activities").json()
    assert email not in activities[activity_name]["participants"]
