#!/usr/bin/python3
"
This  module defines the MyList class"


class MyList(list):
    """A class named MyList"""
    def print_sorted(self):
        """Prints instance"""
        print(sorted(self))
