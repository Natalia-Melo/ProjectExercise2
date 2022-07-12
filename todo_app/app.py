from flask import Flask, render_template, request, redirect, url_for

from todo_app.data.trello_items import fetch_all_cards, create_new_card, mark_as_complete
from todo_app.data.session_items import get_items, add_item
from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())

@app.route('/')
def index():
    items = fetch_all_cards()
    return render_template('index.html', items = items)

@app.route('/add_new_item', methods = ['POST'])
def add_new_item():
    create_new_card(request.form.get('title'))
    return redirect(url_for('index'))


@app.route('/complete_item/<id>')
def complete_item(id):
    print(id)
    mark_as_complete(id)
    return redirect(url_for('index'))
