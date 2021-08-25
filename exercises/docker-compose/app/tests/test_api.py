import pytest
import requests

class TestClassGetRequest:
    def test_status_get(self):
        response = requests.get('http://127.0.0.1:5000/test/service/1n/тип5')
        assert response.status_code, 200
    
class TestClassPutRequest:
    def test_status_post(self):
        response = requests.post('http://127.0.0.1:5000/test/service', data={"id":"10n","name":"new_name"})
        assert response.status_code, 200

    def test_done(self):
        response = requests.get('http://127.0.0.1:5000/test/service/1n/тип5')
        assert response, '{\"info\": \"ok\"}'
