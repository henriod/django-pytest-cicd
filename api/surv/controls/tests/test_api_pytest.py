import json
import pytest
from django.urls import reverse

from controls.models import Control

controls_url = reverse("controls-list")
pytestmark = pytest.mark.django_db

# --------------------------Test Control Get and List ------------------------------------------------
def test_zero_controls_should_return_empty_list(client) -> None:
    response = client.get(controls_url)
    assert response.status_code == 200
    assert json.loads(response.content) == []


# @pytest.fixture
# def muhoroni1() -> Control:
#     return Control.objects.create(name="muhoroni1", cid="fredst", ctype="Primary")


def test_one_control_exist_should_succeed(client, muhoroni1) -> None:
    response = client.get(controls_url)
    response_content = json.loads(response.content)[0]
    assert response.status_code == 200
    assert response_content.get("name") == muhoroni1.name
    assert response_content.get("cid") == "fredst"
    assert response_content.get("ctype") == "Primary"
    assert response_content.get("notes") == ""


# ----------------------Test Control Post --------------------------------------------------------


def test_create_control_without_data_should_fail(client) -> None:
    response = client.post(path=controls_url)
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["This field is required."],
        "cid": ["This field is required."],
    }


def test_create_existing_controls_should_fails(client) -> None:
    Control.objects.create(name="kisumu1", cid="ksm1")
    response = client.post(path=controls_url, data={"name": "kisumu1", "cid": "ksm1"})
    assert response.status_code == 400
    assert json.loads(response.content) == {
        "name": ["control with this name already exists."],
        "cid": ["control with this cid already exists."],
    }


def test_create_control_with_only_name_and_id_all_fields_should_be_default(
    client,
) -> None:
    response = client.post(path=controls_url, data={"name": "muhoroni1", "cid": "mhn1"})
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == "muhoroni1"
    assert response_content.get("cid") == "mhn1"
    assert response_content.get("ctype") == ""
    assert response_content.get("notes") == ""


def test_create_control_with_ctype_primary_should_succeed(client) -> None:
    response = client.post(
        path=controls_url, data={"name": "muhoroni1", "cid": "mhn1", "ctype": "Primary"}
    )
    response_content = json.loads(response.content)
    assert response.status_code == 201
    assert response_content.get("name") == "muhoroni1"
    assert response_content.get("cid") == "mhn1"
    assert response_content.get("ctype") == "Primary"
    assert response_content.get("notes") == ""


@pytest.mark.xfail
def test_should_be_ok_if_fails() -> None:
    pass


@pytest.mark.skip
def test_should_be_skipped() -> None:
    pass


# -----------------------------Learn About Fixtures-----------------------------------------


# @pytest.fixture
# def controls(**kwargs):
#     def _control_factory(**kwargs) -> Control:
#         control_name = kwargs.pop("name", "muhoroni1")
#         control_cid = kwargs.pop("cid", "mhn1")
#         control_ctype = kwargs.pop("ctype", "Secondary")
#         return Control.objects.create(
#             name=control_name, cid=control_cid, ctype=control_ctype, **kwargs
#         )

#     return _control_factory


def test_mutliple_controls_exist_should_succed(client, controls) -> None:
    muhoroni1: Control = controls()
    kisumu1: Control = controls(name="kisumu1", cid="ksm1", ctype="Secondary")
    mlolongo1: Control = controls(name="mlolongo1", cid="mlg1", ctype="Secondary")
    control_names = {muhoroni1.name, kisumu1.name, mlolongo1.name}
    response_controls = client.get(controls_url).json()
    assert len(control_names) == len(response_controls)
    response_control_names = set(
        map(lambda control: control.get("name"), response_controls)
    )
    assert control_names == response_control_names
