import json
from unittest.mock import patch
from django.core import mail


def test_send_email_should_succeed(mailoutbox, settings) -> None:
    settings.EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"
    assert len(mail.outbox) == 0
    # Send message
    mail.send_mail(
        subject="TestSubject Here.",
        message="Test Here is the message.",
        from_email="testemail@gmail.com",
        recipient_list=["testemail2@gmail.com"],
        fail_silently=False,
    )
    # Test that one message has been sent.
    assert len(mailoutbox) == 1

    # Verify that the subject of the first message is correct.
    assert mailoutbox[0].subject == "TestSubject Here."


def test_send_email_without_arguments_should_send_empty_email(client) -> None:
    with patch("controls.views.send_mail") as mocked_send_mail_function:
        response = client.post("/send-email")
        response_content = json.loads(response.content)
        assert response.status_code == 200
        assert response_content["status"] == "success"
        assert response_content["info"] == "email sent successfully"
        mocked_send_mail_function.assert_called_with(
            subject=None,
            message=None,
            from_email="test12django@gmail.com",
            recipient_list=["odhiambo.benard55@gmail.com"],
        )


def test_send_email_with_get_verb_should_fail(client) -> None:
    response = client.get("/send-email")
    assert response.status_code == 405
    assert json.loads(response.content) == {"detail": 'Method "GET" not allowed.'}
