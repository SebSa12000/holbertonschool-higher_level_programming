#!/usr/bin/python3
'''
    Class verboselist2
'''


class VerboseList(list):
    ''' surcharge append '''
    def append(self, value):
        print(f"Added [{value}] to the list.")
        super().append(value)

    ''' surcharge extend '''
    def extend(self, value):
        super().extend(value)
        print(f"Extended the list with [{len(value)}] items.")

    ''' surcharge remove '''
    def remove(self, value):
        print(f"Removed [{value}] from the list.")
        super().remove(value)

    ''' surcharge '''
    def pop(self, item=-1):
        print("Popped [{}] form the list.".format(self[item]))
        super().pop(item)
