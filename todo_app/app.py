from flask import Flask, render_template, request, redirect, url_for

from todo_app.data.trello_items import fetch_all_cards, create_new_card, mark_as_complete, define_lists_in_board
from todo_app.flask_config import Config
from todo_app.data.view_model import Item

def create_app():
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

    return app

