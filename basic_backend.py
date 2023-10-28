import mvc_exceptions as mvc_exc

items= list()

def create_items(app_items):
    global items
    items = app_items
    
def create_item(name, price, quantity):
    global items
    results = list(filter(lambda x: x['name'] == name, items))
    if results:
        raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
    else:
        items.append({'name': name, 'price': price, 'quantity': quantity})
    
def read_item(name):
    global items
    myitems = list(filter(lambda x: x['name'] == name, items))
    if myitems:
        return myitems[0]
    else:
        raise mvc_exc.ItemNotStored(
            'Can\'t read "{}" because it\'s not stored'.format(name)
        )

def read_items():
    global items
    return [item for item in items]


def update_item(name, price, quantity):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items))
        )
    if idxs_items:    
        i, item_to_update = idxs_items[0][0], idxs_items[0][1]
        items[i] = {'name': name, 'price': price, 'quantity': quantity}
    else:
        raise mvc_exc.ItemNotStored(
            'Cannot update "{}" because it is not stored'.format(name)
        )

def delete_item(name):
    global items
    idxs_items = list(
        filter(lambda i_x: i_x[1]['name'] == name, enumerate(items))
    )        
    if idxs_items:
        i, items_to_delete = idxs_items[0][0], idxs_items[0][1]
        del items[i]
    else:
        raise mvc_exc.ItemNotStored(
            'Cannot delete "{}" because it is not stored'.format(name)
        )
        
