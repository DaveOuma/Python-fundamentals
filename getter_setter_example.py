#!/usr/bin/python3

Class Student:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name

    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age
        
