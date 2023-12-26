from . import basic_backend

class ModelBasic(object):
    
    def __init__(self, application_items) -> None:
        self._item_type = 'product'
        self.create_items(application_items)
        
    @property
    def item_type(self):
        return self._item_type
    
    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type
    
    def create_item(self, name, price, quantity):
        basic_backend.create_item(name, price, quantity)
        

    def create_items(self, items):
        basic_backend.create_items(items)

    def read_item(self, name):
        return basic_backend.read_item(name)

    def read_items(self):
        return basic_backend.read_items()

    def update_item(self, name, price, quantity):
        basic_backend.update_item(name, price, quantity)

    def delete_item(self, name):
        basic_backend.delete_item(name)