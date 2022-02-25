import json
import pytest
import requests

testing_env_controls_url = "http://127.0.0.1:8000/controls/"

# ----------------------This test will fail in CI since it will look for testing env localhost----------------
@pytest.mark.skip_in_ci
def test_zero_controls_django_agnostic() -> None:
    response = requests.get(url=testing_env_controls_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


@pytest.mark.skip_in_ci
def test_create_existing_controls_django_agnostics() -> None:
    response = requests.post(
        url=testing_env_controls_url,
        data={"name": "mlolongo", "cid": "mlg1", "ctype": "Secondary"},
    )
    assert response.status_code == 201
    response_content = json.loads(response.content)
    assert response_content.get("name") == "mlolongo"

    cleanup_control(control_id=response_content["id"])


@pytest.mark.skip_in_ci
def cleanup_control(control_id: str) -> None:
    response = requests.delete(url=f"http://127.0.0.1:8000/controls/{control_id}")
    assert response.status_code == 204


# -------------Morking test with responses library--------------------------------------------------------------------------
@pytest.mark.crypto
def test_dogecoin_api() -> None:
    response = requests.get(
        url="https://api.cryptonator.com/api/ticker/doge-usd",
        headers={"User-Agent": "Mozilla/5.0"},
    )

    assert response.status_code == 200
    response_content = json.loads(response.content)
    assert response_content["ticker"]["base"] == "DOGE"
    assert response_content["ticker"]["target"] == "USD"


import responses


@pytest.mark.crypto
@responses.activate
def test_mocked_dogecoin_api() -> None:
    responses.add(
        method=responses.GET,
        url="https://api.cryptonator.com/api/ticker/doge-usd",
        json={
            "ticker": {
                "base": "EDEN",
                "target": "EDEN-USD",
                "price": "0.04535907",
                "volume": "4975940509.75870037",
                "change": "-0.00052372",
            },
            "timestamp": 1612515303,
            "success": True,
            "error": "",
        },
        status=200,
    )
    response = requests.get(
        url="https://api.cryptonator.com/api/ticker/doge-usd",
        headers={"User-Agent": "Mozilla/5.0"},
    )

    assert response.status_code == 200
    response_content = json.loads(response.content)
    assert response_content["ticker"]["base"] == "EDEN"
    assert response_content["ticker"]["target"] == "EDEN-USD"
