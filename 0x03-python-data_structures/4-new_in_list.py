#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > range(len(my_list) - 1):
        return my_list
    cpy_list = [num for num in my_list]
    cpy_list[idx] = element
    return cpy_list
