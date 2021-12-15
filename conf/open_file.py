import json


def open_file(files):
    with open(files, 'r') as fi:
        return json.load(fi)
