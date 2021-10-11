def create_inventory(items):
    """

    :param items: list - list of items to create an inventory from.
    :return:  dict - the inventory dictionary.
    """
    item_name = set(items)
    inventory = {}
    for item in item_name:
        item_amount = sum([n == item for n in items])
        inventory[item] = item_amount

    return inventory


def add_items(inventory, items):
    """

    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    item_name = set(items)

    for item in item_name:
        item_amount = sum([n == item for n in items])

        if item in inventory:
            inventory[item] += item_amount
        else:
            inventory[item] = item_amount

    return inventory


def decrement_items(inventory, items):
    """

    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    item_name = set(items)

    for item in item_name:
        item_amount = sum([n == item for n in items])
        if inventory[item] > item_amount:
            inventory[item] -= item_amount
        else:
            inventory[item] = 0

    return inventory


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    if item in inventory:
        del inventory[item]
    return inventory


def list_inventory(inventory):
    """

    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """
    return [(item, amount) for item, amount in inventory.items() if amount > 0]
