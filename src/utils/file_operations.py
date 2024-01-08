import json


def write_to_json(data, path):
    with open(path, 'w') as file:
        json.dump(data, file, indent=4)


def read_from_json(path):
    with open(path, 'r') as file:
        data = json.load(file)
    return data
