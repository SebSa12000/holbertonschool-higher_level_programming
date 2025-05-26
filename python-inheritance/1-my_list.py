#!/usr/bin/python3
''' Mylist '''
class MyList(list):

    ''' Mylist class that inherits from list '''
    def __init__(self):
        super().__init__()  

    def print_sorted(self):
        ''' Print the list in sorted order '''
        sorted_list = sorted(self)
        print(sorted_list)  

    def __str__(self):
        ''' String representation of the list '''
        return str(self)
