#!/usr/bin/python3

"""
add argument to python
list and save them
to a file
"""
from sys import argv
from os import path


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


if path.exists("add_item.json"):
    py_list = load_from_json_file("add_item.json")
else:
    py_list = []
py_list += argv[1:]
save_to_json_file(py_list, "add_item.json")
