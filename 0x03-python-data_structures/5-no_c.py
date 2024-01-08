#!/usr/bin/python3
def no_c(my_string):
    our_string = ""
    for n in range(len(my_string)):
        if my_string[n] != 'C' and my_string[n] != 'c':
            our_string += my_string[n]
    return (our_string)
