#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json


class FileStorage:
    """This class manages storage for hbnb models in json format"""
    __file_path__ = 'file.json'
    __objects = {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects
    
    def new(self,obj):
        """"Adds a new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] +'.'+obj.id:obj})
        