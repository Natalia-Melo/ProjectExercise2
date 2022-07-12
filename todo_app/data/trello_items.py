import requests
import os

url_main = 'https://api.trello.com/1/cards/'

def fetch_all_cards():
    r_json = json_of_all_cards()
    return r_json

def create_new_card(title):
    url = url_main
    query = {'idList':'62cc1c1efb40f28f8a02eac2', 'key': os.environ.get('key'),
             'token': os.environ.get('token'),'name':title}
    headers = {
        "Accept": "application/json"
    }

    r = requests.request("POST", url, params=query, headers=headers)

def mark_as_complete(card_id):
    query = {'idList':'62cc1c1efb40f28f8a02eac4', 'key': os.environ.get('key'),
             'token': os.environ.get('token')}

    url = url_main+card_id

    headers = {
        "Accept": "application/json"
    }
    r = requests.put(url, params=query, headers=headers)

def json_of_all_cards():
    Board_ID = '62cc1c1efb40f28f8a02eabb'
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/cards/open'

    query_parameters = {'key': os.environ.get('key'),
                                'token': os.environ.get('token')}

    r = requests.get(url, params=query_parameters)

    r_json = r.json()
    return r_json


