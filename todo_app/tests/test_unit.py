from todo_app.data.Item import Item
from todo_app.data.view_model import ViewModel

initialise_list = [
    Item(1,'Example 1','123','Desc','To-Do').items,
    Item(2,'Example 2','123','Desc','To-Do').items,
    Item(3,'Example 3','456','Desc','Doing').items,
    Item(4,'Example 4','789','Desc','Done').items
]

object = ViewModel(initialise_list)

def test_doing():
    assert object.to_do_items == ['Example 1', 'Example 2']

def test_to_do():
    assert object.doing_items == ['Example 3']

def test_done():
    assert object.done_items == ['Example 4']