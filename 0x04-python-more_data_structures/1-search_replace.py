#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rslt = []
    for i in my_list:
        if i == search:
            rslt.append(replace)
        else:
            rslt.append(i)
    return rslt
