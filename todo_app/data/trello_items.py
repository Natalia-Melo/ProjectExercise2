import requests
import os

url_main_cards = 'https://api.trello.com/1/cards/'
Board_ID = os.environ.get('BOARD_ID')
base_query_parameters = {'key': os.environ.get('key'),
                                'token': os.environ.get('token')}

def fetch_all_cards():
    r_json = json_of_all_cards()
    return r_json

def create_new_card(title):
    url = url_main_cards
    data_todo_list = (define_lists_in_board())[0]

    query = base_query_parameters
    query.update({'name':title})
    query.update({'idList':data_todo_list['idList']})

    headers = {
        "Accept": "application/json"
    }

    r = requests.request("POST", url, params=query, headers=headers)

def mark_as_complete(card_id):
    data_done_list = (define_lists_in_board())[-1]
    query = base_query_parameters
    query.update({'idList':data_done_list['idList']})

    url = url_main_cards+card_id

    headers = {
        "Accept": "application/json"
    }
    r = requests.put(url, params=query, headers=headers)

def json_of_all_cards():
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/cards/open'

    query_parameters = base_query_parameters

    r = requests.get(url, params=query_parameters)

    r_json = r.json()
    return r_json

def define_lists_in_board():
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/lists/open'

    query_parameters = base_query_parameters

    r = requests.get(url, params=query_parameters)
    r_json = r.json()
    lists_in_boards = []

    for item in r_json:
        lists_in_boards.append({'idList':item['id'], 'name':item['name']})
    return lists_in_boards

