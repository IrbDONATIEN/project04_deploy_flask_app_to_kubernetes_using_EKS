'''
Tests for jwt flask app.
'''
import os
import json
import pytest

import main

SECRET = 'TestSecret'
TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2Njc1NjE3MjcsIm5iZiI6MTY2NjM1MjEyNywiZW1haWwiOiJ3b2xmQHRoZWRvb3IuY29tIn0.JfHs3nCw_BEerIiLu3g2TJUw8CWUFOg2n5AXrF-Ksec'
EMAIL = 'wolf@thedoor.com'
PASSWORD = 'huff-puff'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    main.APP.config['TESTING'] = False
    client = main.APP.test_client()

    yield client



def test_health(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == 'Healthy'


def test_auth(client):
    body = {'email': EMAIL,
            'password': PASSWORD}
    response = client.post('/auth', 
                           data=json.dumps(body),
                           content_type='application/json')

    assert response.status_code == 200
    token = response.json['token']
    assert token is not None
