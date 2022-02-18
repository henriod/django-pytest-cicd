import json
from unicodedata import name
from urllib import response
import pytest
from unittest import TestCase
from django.test import Client
from django.urls import reverse

from controls.models import Control

@pytest.mark.django_db
class BasicControlApiTestCase(TestCase):
    def setUp(self)-> None:
        self.client = Client()
        self.controls_url = reverse("controls-list")
    def tearDown(self) -> None:
        pass

class TestControls(BasicControlApiTestCase):   
    
    def test_zero_controls_should_return_empty_list(self)->None:
        response = self.client.get(self.controls_url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content),[])

    def test_one_control_exist_should_succeed(self)->None:
        muhoroni1 = Control.objects.create(name="muhoroni1", cid="fredst", ctype="Primary")
        response = self.client.get(self.controls_url)
        response_content = json.loads(response.content)[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_content.get("name"), muhoroni1.name)
        self.assertEqual(response_content.get("cid"), "fredst")
        self.assertEqual(response_content.get("ctype"), "Primary")
        self.assertEqual(response_content.get("notes"), "")

        muhoroni1.delete()

class TestControlPost(BasicControlApiTestCase):
    def test_create_control_without_data_should_fail(self)->None:
        response = self.client.post(path=self.controls_url)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            json.loads(response.content),{"name": ["This field is required."],"cid": ["This field is required."]}
        )

    def test_create_existing_controls_should_fails(self)-> None:
        Control.objects.create(name ="kisumu1", cid="ksm1")
        response = self.client.post(path=self.controls_url, data={"name":"kisumu1","cid":"ksm1"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content),{"name": ["control with this name already exists."], "cid": ["control with this cid already exists."]}
        )

    def test_create_control_with_only_name_and_id_all_fields_should_be_default(self)->None:
        response = self.client.post(path=self.controls_url, data={"name":"muhoroni1","cid":"mhn1"})
        response_content = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_content.get("name"),"muhoroni1")
        self.assertEqual(response_content.get("cid"),"mhn1")
        self.assertEqual(response_content.get("ctype"),"")
        self.assertEqual(response_content.get("notes"),"")

    def test_create_control_with_ctype_primary_should_succeed(self)->None:
        response = self.client.post(path=self.controls_url, data={"name":"muhoroni1","cid":"mhn1","ctype":"Primary"})
        response_content = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_content.get("name"),"muhoroni1")
        self.assertEqual(response_content.get("cid"),"mhn1")
        self.assertEqual(response_content.get("ctype"),"Primary")
        self.assertEqual(response_content.get("notes"),"")


