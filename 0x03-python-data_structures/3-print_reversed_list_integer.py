#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rl = my_list.reverse()
    for i in rl:
        print("{:d}".format(i))
