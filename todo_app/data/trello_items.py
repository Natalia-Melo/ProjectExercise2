import requests
import os

Board_ID = os.environ.get('BOARD_ID')

def build_url(endpoint):
    return 'https://api.trello.com/1/'+endpoint

def get_auth_params():
    return({'key':os.environ.get('KEY'), 'token':os.environ.get('TOKEN')})

def build_params(params = {}):
    full_params = get_auth_params()
    full_params.update(params)
    return full_params

def fetch_all_cards():
    r_json = json_of_all_cards()
    return r_json

def create_new_card(title):
    url = build_url('cards')

    data_todo_list = (define_lists_in_board())[0]

    query = build_params({'name':title,'idList':data_todo_list['idList']})

    headers = {
        "Accept": "application/json"
    }
    r = requests.request("POST", url, params=query, headers=headers)

def mark_as_complete(card_id):
    url = build_url('cards/'+card_id)
    data_done_list = (define_lists_in_board())[-1]

    query = build_params({'idList':data_done_list['idList']})

    headers = {
        "Accept": "application/json"
    }
    r = requests.put(url, params=query, headers=headers)

def json_of_all_cards():
    url = build_url('boards/'+Board_ID + '/cards/open')

    query = get_auth_params()

    r = requests.get(url, params=query)

    r_json = r.json()
    return r_json

def define_lists_in_board():
    url = build_url('boards/'+Board_ID + '/lists/open')

    query = get_auth_params()

    r = requests.get(url, params=query)
    r_json = r.json()
    lists_in_boards = []
    for item in r_json:
        lists_in_boards.append({'idList':item['id'], 'name':item['name']})
    return lists_in_boards
