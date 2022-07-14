class Item:
    def __init__(self, id, name,idList,desc):
        self.id = id
        self.name = name
        self.idList = idList
        self.desc = desc
        self._items = [self.id, self.name, self.idList,self.desc]

    @property
    def items(self):
        return self._items

    @property
    def doing_items(self):
        return [item['name'] for item in self._items if item['status']=='Doing']

    @property
    def to_do_items(self):
        return [item['name'] for item in self._items if item['status']=='To-Do']

    @property
    def done_items(self):
        return [item['name'] for item in self._items if item['status']=='Done']