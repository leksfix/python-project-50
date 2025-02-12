import json

from yaml import Loader, load


def parse_json(filename):
    return json.load(open(filename))


def parse_yaml(filename):
    return load(open(filename), Loader=Loader)