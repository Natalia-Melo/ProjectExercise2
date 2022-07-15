import os
from time import sleep
from threading import Thread
from todo_app import app
from todo_app.data.trello_items import create_new_board, delete_board
import pytest

@pytest.fixture(scope='module')
def app_with_temp_board():
    board_id = create_new_board()
    os.environ['BOARD_ID'] = board_id
    application = app.create_app()

    thread = Thread(target=lambda:
    application.run(use_reloader=False))
    thread.daemon = True
    thread.start()

    # Give the app a moment to start
    sleep(1)
    yield application
    # Tear Down
    thread.join(1)
    delete_board(board_id)