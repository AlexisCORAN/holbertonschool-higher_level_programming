#!/usr/bin/python3
"""
This module defines the "Student" class
"""


class Student:
    """Representation of a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance
        with specified attributes"""
        class_dic = self.__dict__
        sel_dic = dict()

        if type(attrs) is list:
            for attr in attrs:
                if type(attr) is not str:
                    return class_dic

                if attr in class_dic:
                    sel_dic[attr] = class_dic[attr]

            return sel_dic
        else:
            return class_dic
