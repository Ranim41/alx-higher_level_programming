#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        pass
    else:
        my_list.reverse()
        for num in range(len(my_list)):
            print('{:d}'.format(my_list[num]))
