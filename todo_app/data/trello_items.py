import requests
import os

def build_url(endpoint):
    return f"https://api.trello.com/1/{endpoint}"

def get_auth_params():
    return({'key':os.environ.get('KEY'), 'token':os.environ.get('TOKEN')})

def build_params(params = {}):
    full_params = get_auth_params()
    full_params.update(params)
    return full_params

def create_new_card(title):
    url = build_url('cards')
    data_todo_list = (define_lists_in_board())[0]
    query = build_params({'name':title,'idList':data_todo_list['idList']})
    headers = {
        "Accept": "application/json"
    }
    requests.post(url, params=query, headers=headers)

def mark_as_complete(card_id):
    url = build_url(f"cards/{card_id}")
    data_done_list = (define_lists_in_board())[-1]
    query = build_params({'idList':data_done_list['idList']})
    headers = {
        "Accept": "application/json"
    }
    requests.put(url, params=query, headers=headers)

def fetch_all_cards():
    Board_ID = os.environ.get('BOARD_ID')
    url = build_url(f"boards/{Board_ID}/cards/open")
    query = get_auth_params()
    r = requests.get(url, params=query)
    r_json = r.json()
    return r_json

def define_lists_in_board():
    Board_ID = os.environ.get('BOARD_ID')
    url = build_url(f"boards/{Board_ID}/lists/open")
    query = get_auth_params()
    r = requests.get(url, params=query)
    r_json = r.json()
    return [{'idList':item['id'], 'name':item['name']} for item in r_json]


def delete_board(board_id_delete):
    url = build_url(f"boards/{board_id_delete}")
    query = get_auth_params()
    requests.delete(url,params=query)


def create_new_board(name_new_board):
    url = build_url(f"boards/")
    query = get_auth_params({'name':name_new_board})
    requests.post(url, params=query)