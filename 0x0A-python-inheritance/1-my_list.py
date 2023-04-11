#!/usr/bin/python3

"""
MyList class that
inherit from list
"""


class MyList(list):
    """
    MyList class
    """

    def print_sorted(self):
        """
        instance method that sort the
        list integer element in ascending order
        and print the sorted list
        """
        ordered_list = []
        cnt = range(len(self))
        for j in cnt:
            least = min(self)
            ordered_list.append(least)
            self.remove(least)
        print(ordered_list)
