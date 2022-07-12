import requests
import os

# LIST_ID = [{'to-do-list_id': '62cc1c52bb382e686252622d'},
           #{'board' : '62cc1c1efb40f28f8a02eabb'}]

def fetch_all_cards():
    r_json = json_of_all_cards()
    return r_json
    output_list = []
    for item in r_json:
        output_list.append(item['name'])

    #return output_list

def create_new_card(title):
    # Board_ID = '62cc1c1efb40f28f8a02eabb'
    url = 'https://api.trello.com/1/cards'

    #query_parameters = {'key': '96232fa3a30653ad5263af0c8c1df055',
                                #'token': '24fd9ec4f8fa09ab74fcc9c23da319308c1bf094ec9e69a4da7202768c0d6441'}

    query = {'idList':'62cc1c1efb40f28f8a02eac3', 'key': '96232fa3a30653ad5263af0c8c1df055',
             'token': '24fd9ec4f8fa09ab74fcc9c23da319308c1bf094ec9e69a4da7202768c0d6441','name':title}
    headers = {
        "Accept": "application/json"
    }

    r = requests.request("POST", url, params=query, headers=headers)


def mark_as_complete(card_id):
    query = {'idList':'62cc1c1efb40f28f8a02eac4', 'key': '96232fa3a30653ad5263af0c8c1df055',
             'token': '24fd9ec4f8fa09ab74fcc9c23da319308c1bf094ec9e69a4da7202768c0d6441'}

    url = 'https://api.trello.com/1/cards/'+card_id

    headers = {
        "Accept": "application/json"
    }

    r = requests.put(url, params=query, headers=headers)

def json_of_all_cards():
    Board_ID = '62cc1c1efb40f28f8a02eabb'
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/cards/open'

    query_parameters = {'key': '96232fa3a30653ad5263af0c8c1df055',
                                'token': '24fd9ec4f8fa09ab74fcc9c23da319308c1bf094ec9e69a4da7202768c0d6441'}

    r = requests.get(url, params=query_parameters)

    r_json = r.json()
    return r_json


class Item:
    def __init__(self, id, name, status = 'To Do'):
        self.id = id
        self.name = name
        self.status = status \

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])
