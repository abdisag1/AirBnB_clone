<<<<<<< HEAD
#!usr/bin/python3
"""

"""


from models.base_model import BaseModel
import json

classes = {"BaseModel": BaseModel}


class FileStorage:
    """

    """
=======
#!/usr/bin/python3
"""
Contains the FileStorage class
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """serializes instances to a JSON and deserializes JSON to instances"""

>>>>>>> 6c99573bd458e64cd849b3d22e022e063d160b9d
    __file_path = "file.json"
    __objects = {}

    def all(self):
<<<<<<< HEAD
        return self.__objects

    def new(self, obj):
        ind = obj.__class__.__name__ + "." + obj.id
        self.__objects[ind] = obj

    def save(self):
         """serializes __objects to the JSON file (path: __file_path)"""
         json_objects = {}
         for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
         with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
=======
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        ind = obj.__class__.__name__ + '.' + obj.id
        self.__objects[ind] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        diction = {}
        for x in self.__objects:
            diction[x] = self.__objects[x].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(diction, f)

    def reload(self):
        """  deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, "r") as f:
                jo = json.load(f)
            for o in jo.values():
                cls_name = o["__class__"]
                del o["__class__"]
                self.new(eval(cls_name)(**o))
>>>>>>> 6c99573bd458e64cd849b3d22e022e063d160b9d
        except:
            pass
