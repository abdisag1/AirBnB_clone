#!/usr/bin/python3
"""
Contains the FileStorage class
"""


class FileStorage:
    """serializes instances to a JSON and deserializes JSON to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects
