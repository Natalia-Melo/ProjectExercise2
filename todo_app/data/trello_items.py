import requests
import os

# Lists information
LISTS_INFO = [{'id': 1, 'name': 'To Do', 'trello_id':'62cc1c1efb40f28f8a02eac2'},
              {'id': 2, 'name': 'Doing', 'trello_id':'62cc1c1efb40f28f8a02eac3'},
              {'id': 3, 'name': 'Done', 'trello_id': '62cc1c1efb40f28f8a02eac4'}
              ]


def fetch_all_cards():
    r_json = json_of_all_cards()
    return r_json

def create_new_card(title):
    # Board_ID = '62cc1c1efb40f28f8a02eabb'
    url = 'https://api.trello.com/1/cards'

    query = {'idList':'62cc1c1efb40f28f8a02eac3', 'key': os.environ.get('key'),
             'token': os.environ.get('token'),'name':title}
    headers = {
        "Accept": "application/json"
    }

    r = requests.request("POST", url, params=query, headers=headers)

def mark_as_complete(card_id):
    query = {'idList':'62cc1c1efb40f28f8a02eac4', 'key': os.environ.get('key'),
             'token': os.environ.get('token')}

    url = 'https://api.trello.com/1/cards/'+card_id

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


