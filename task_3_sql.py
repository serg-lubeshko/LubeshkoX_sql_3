import json
import os


def open_file(files):
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir, files)
    with open(file_path, 'r') as fi:
        return json.load(fi)

print(list(open('students.json')))