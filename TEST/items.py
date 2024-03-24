import json
import random


def load_items_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    items = {}
    for item in data["items"]:
        if isinstance(item["damage"], list):
            damage = random.randint(item["damage"][0], item["damage"][1])
        else:
            damage = item["damage"]
        items[item["id"]] = [item["name"], damage, item["range"], item["cost"]]
    return items

items = load_items_from_json('items.json')

def printItems():
    print(items)
