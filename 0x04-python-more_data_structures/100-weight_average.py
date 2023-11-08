#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        denomin = 0
        nomin = 0
        for i in my_list:
            nomin += i[0] * i[1]
            denomin += i[1]
    return nomin / denomin
