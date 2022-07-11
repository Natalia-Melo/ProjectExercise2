import requests
import os

LIST_ID = [{'to-do-list_id': '62cc1c52bb382e686252622d'},
           {'board' = '62cc1c1efb40f28f8a02eabb'}]

def fetch_all_cards(Board_ID):
    Board_ID = '62cc1c1efb40f28f8a02eabb'
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/cards/open'

    query_parameters = {'key' : '96232fa3a30653ad5263af0c8c1df055',
                                'token' : '24fd9ec4f8fa09ab74fcc9c23da319308c1bf094ec9e69a4da7202768c0d6441'}

    r = requests.get(url, params=query_parameters)

    r_json = r.json()

    output_list = []
    for item in r_json:
        output_list.append(item['name'])

    return output_list

def create_new_card(title):
    Board_ID = '62cc1c1efb40f28f8a02eabb'
    to_do_list_id = '62cc1c52bb382e686252622d'
    url = 'https://api.trello.com/1/boards/'+Board_ID + '/cards'

    query = {'idList':'62cc1c52bb382e686252622d', 'key' : os.environ.get('key'), 'token' : os.environ.get('token'),
             'name' = title}

    r = requests.post(url, params=query)



