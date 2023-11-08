#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    rslt = []
    sls = []
    for i in matrix:
        for j in i:
            sls.append(j * j)
        rslt.append(sls)
        sls = []

    return rslt
