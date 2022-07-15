import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests
import os


@pytest.fixture
def client():
     # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    #  Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
         yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', stub)
    response = client.get('/')
    r = response.data.decode()
    assert response.status_code == 200
    assert 'Test Card' in response.data.decode()

def stub(url, params={}):
    test_board_id = os.environ.get('BOARD_ID')
    fake_response_data = []
    if url == f'https://api.trello.com/1/boards/{test_board_id}/lists/open':
        fake_response_data = [{
            'id': '6564f',
            'name':'Done'
        }]
    elif url == f"https://api.trello.com/1/boards/{test_board_id}/cards/open":
        fake_response_data = [{
            'id': '123def',
            'name': 'Test Card',
            'idList': '6564f',
            'desc': 'Test Description'
        }]
    return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data