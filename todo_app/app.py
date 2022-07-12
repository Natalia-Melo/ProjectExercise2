from flask import Flask, render_template, request, redirect, url_for

from todo_app.data.trello_items import fetch_all_cards, create_new_card, mark_as_complete, define_lists_in_board
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = fetch_all_cards()

    lists = define_lists_in_board()

    all_items = [Item(item['id'],item['name'],item['idList'],item['desc']) for item in items]

    return render_template('index.html', items = all_items, lists = lists)

@app.route('/add_new_item', methods = ['POST'])
def add_new_item():
    create_new_card(request.form.get('title'))
    return redirect(url_for('index'))


@app.route('/complete_item/<id>')
def complete_item(id):
    mark_as_complete(id)
    return redirect(url_for('index'))


class Item:
    def __init__(self, id, name,idList,desc):
        self.id = id
        self.name = name
        self.idList = idList
        self.desc = desc

    @classmethod
    def from_trello_card(cls, card, list):
        return cls(card['id'], card['name'], list['name'])

