class Item:
    def __init__(self, id, name,idList,desc,listName = ''):
        self.id = id
        self.name = name
        self.idList = idList
        self.desc = desc
        self.status = listName
        self._items = [self.id, self.name, self.idList,self.desc,self.status]

    @property
    def items(self):
        return self._items
