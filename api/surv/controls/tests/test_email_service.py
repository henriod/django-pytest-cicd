from http import client
import json
import re
from unittest.mock import patch
from urllib import response
from django.test import Client, TestCase
from django.core import mail


class EmailUnitTest(TestCase):
    def test_send_email_should_succeed(self)->None:
        with self.settings(
            EMAIL_BACKEND ="django.core.mail.backends.locmem.EmailBackend"
        ):
            self.assertEqual(len(mail.outbox), 0)
            # Send message
            mail.send_mail(
                subject="TestSubject Here.",
                message= "Test Here is the message.",
                from_email="testemail@gmail.com",
                recipient_list=["testemail2@gmail.com"],
                fail_silently=False,
            )
            # Test that one message has been sent.
            self.assertEqual(len(mail.outbox), 1)

            #Verify that the subject of the first message is correct.
            self.assertEqual(mail.outbox[0].subject,"TestSubject Here." )

    def test_send_email_without_arguments_should_send_empty_email(self)-> None:
        client = Client()
        with patch(
            "controls.views.send_mail"
        ) as mocked_send_mail_function:
            response = client.post(path='/send-email')
            response_content = json.loads(response.content)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response_content['status'], 'success')
            self.assertEqual(response_content['info'], 'email sent successfully')
            mocked_send_mail_function.assert_called_with(
                subject = None,
                message =None,
                from_email= "test12django@gmail.com",
                recipient_list =["odhiambo.benard55@gmail.com"]
            )
    def test_send_email_with_get_verb_should_fail(self)->None:
        client = Client()
        response = client.get(path="/send-email")
        assert response.status_code==405
        assert json.loads(response.content) == {"detail": "Method \"GET\" not allowed."}