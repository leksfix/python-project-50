import json

from yaml import Loader, load


def get_extension(filename):
    return str(filename).split('.')[-1].lower()


def parse_json(filename):
    return json.load(open(filename))


def parse_yaml(filename):
    return load(open(filename), Loader=Loader)


def parse_file(filename):
    ext = get_extension(filename)
    if ext == 'json':
        return parse_json(filename)
    elif ext in {'yml', 'yaml'}:
        return parse_yaml(filename)
    else:
        raise ValueError(f"Unknown file type: '{ext}'")

