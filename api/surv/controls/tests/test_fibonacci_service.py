import json
from unittest.mock import patch

def test_get_the_nth_positive_int_fibonacci_number_succeed(client) -> None:
    response = client.post(path="/fibonacci", data={"fibonacci":40})
    assert response.status_code == 200
    assert json.loads(response.content) == {"status": "success","infor": "the n'th fibonacci number is :102334155 "}

def test_get_the_nth_negative_int_fibonacci_number_fails(client) -> None:
    response = client.post(path="/fibonacci", data={"fibonacci":-40})
    assert response.status_code == 406
    assert json.loads(response.content) == {"status": "failed","infor": "n'th:-40 must be positive interger number"}

def test_get_the_nth_fibonacci_number_with_no_arguments_fails(client) -> None:
    response = client.post(path="/fibonacci")
    assert response.status_code == 406
    assert json.loads(response.content) == {"status": "failed","infor": "n'th:None must be positive interger number"}
