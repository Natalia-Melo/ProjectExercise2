class ViewModel:
    def __init__(self,items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def doing_items(self):
        return [item[1] for item in self.items if item[4]=='Doing']

    @property
    def to_do_items(self):
        return [item[1] for item in self.items if item[4]=='To-Do']

    @property
    def done_items(self):
        return [item[1] for item in self.items if item[4]=='Done']

