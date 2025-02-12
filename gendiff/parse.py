import json


def parse_json(filename):
    return json.load(open(filename))
