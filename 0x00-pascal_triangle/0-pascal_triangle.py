#!/usr/bin/python3
""" Module for Pascal's triangle """


def pascal_triangle(n):
    """ Function for Pascal's triangle """
    if (n <= 0):
        return []
    t = []
    for i in range(1, n+1):
        r = []
        for j in range(1, i+1):
            if (j == 1 or j == i):
                r.append(1)
            else:
                r.append(t[i-2][j-1] + t[i-2][j-2])
        t.append(r)
    return t
