import json
from urllib import response
import pytest
import requests

testing_env_controls_url = "http://127.0.0.1:8000/controls/"

#----------------------This test will fail in CI since it will look for testing env localhost----------------
@pytest.mark.skip_in_ci
def test_zero_controls_django_agnostic() -> None:
    response = requests.get(url=testing_env_controls_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []
    
@pytest.mark.skip_in_ci
def test_create_existing_controls_django_agnostics() -> None:
    response = requests.post(url=testing_env_controls_url, data={"name": "mlolongo", "cid": "mlg1","ctype":"Secondary"})
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "mlolongo"

    cleanup_control(control_id=response_content["id"])
@pytest.mark.skip_in_ci
def cleanup_control(control_id: str)-> None:
    response = requests.delete(url=f"http://127.0.0.1:8000/controls/{control_id}")
    assert response.status_code == 204
