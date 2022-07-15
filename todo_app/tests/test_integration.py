import pytest
from dotenv import load_dotenv, find_dotenv
from todo_app import app
import requests
import os


@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    test_app = app.create_app()
    with test_app.test_client() as client:
         yield client

def test_index_page(monkeypatch, client):
    monkeypatch.setattr(requests, 'get', stub)
    response = client.get('/')
    assert response.status_code == 200
    assert 'Test Card' in response.data.decode()

def test_create_new_page(monkeypatch, client):
    monkeypatch.setattr(requests,'get', stub)
    monkeypatch.setattr(requests,'post', new_stub)
    response = client.post('/add_new_item')
    assert response.status_code == 302 # After post requet, page sends you back to the main page

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

def new_stub(url, params={}, headers={}):
    fake_response_data = []
    if url == f"https://api.trello.com/1/cards":
        fake_response_data = [{
            'name': 'Test Card2',
            'idList': '6564f',
        }]

    return StubResponse(fake_response_data)
    raise Exception(f'Integration test did not expect URL "{url}"')

class StubResponse():
    def __init__(self, fake_response_data):
        self.fake_response_data = fake_response_data

    def json(self):
        return self.fake_response_data