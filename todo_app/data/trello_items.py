import requests
import os

url_main_cards = 'https://api.trello.com/1/cards/'
Board_ID = os.environ.get('BOARD_ID')


def fetch_all_cards():
    r_json = json_of_all_cards()
    return r_json

def create_new_card(title):
    url = url_main_cards
    data_todo_list = (define_lists_in_board())[0]

    query = {'idList':data_todo_list['idList'], 'key': os.environ.get('key'),
             'token': os.environ.get('token'),'name':title}
    headers = {
        "Accept": "application/json"
    }

    r = requests.request("POST", url, params=query, headers=headers)

def mark_as_complete(card_id):
    data_done_list = (define_lists_in_board())[-1]
    query = {'idList':data_done_list['idList'], 'key': os.environ.get('key'),
             'token': os.environ.get('token')}

    url = url_main_cards+card_id

    headers = {
        "Accept": "application/json"
    }
    r = requests.put(url, params=query, headers=headers)

def json_of_all_cards():
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/cards/open'

    query_parameters = {'key': os.environ.get('key'),
                                'token': os.environ.get('token')}

    r = requests.get(url, params=query_parameters)

    r_json = r.json()
    return r_json

def define_lists_in_board():
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/lists/open'

    query_parameters = {'key': os.environ.get('key'),
                                'token': os.environ.get('token')}

    r = requests.get(url, params=query_parameters)
    r_json = r.json()
    lists_in_boards = []

    for item in r_json:
        lists_in_boards.append({'idList':item['id'], 'name':item['name']})
    return lists_in_boards


