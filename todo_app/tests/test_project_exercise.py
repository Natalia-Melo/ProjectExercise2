from todo_app.data.view_model2 import ViewModel
initialise_list = [
    {'name': 'Example 1', 'status':'Doing'},
    {'name': 'Example 2', 'status':'Doing'},
    {'name': 'Example 3', 'status':'Done'},
    {'name': 'Example 4', 'status': 'To-Do'}
]

def test_doing():
    item = ViewModel(initialise_list)
    assert item.doing_items == ['Example 1', 'Example 2']

def test_to_do():
    item = ViewModel(initialise_list)
    assert item.to_do_items == ['Example 4']

def test_done():
    item = ViewModel(initialise_list)
    assert item.done_items == ['Example 3']