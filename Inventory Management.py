def create_inventory(items):
    inventory = {}
    for item in items:
    # Use the get() method with a default value of 0 for quantity
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


def decrement_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] < 0:
                inventory[item] = 0
        else:
            print(f"Item '{item}' not found in inventory and cannot be decremented.")  
    return inventory


def remove_item(inventory, item):
    if item in inventory:
        inventory.pop(item)
    return inventory


def list_inventory(inventory):
    inventory_list = []
    for key in inventory:
        if inventory[key] > 0:
            inventory_list.append((key, inventory[key]))
    return inventory_list
