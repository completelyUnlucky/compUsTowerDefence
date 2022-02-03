import os
from os import path

directory = os.path.dirname(os.getcwd())


def find_file(file):
    for root, dirs, files in os.walk(directory):
        if file in files:
            return os.path.join(root, file)


def find_pack(pack):
    for root, dirs, files in os.walk(directory):
        if pack in dirs:
            return os.path.join(root, pack)
