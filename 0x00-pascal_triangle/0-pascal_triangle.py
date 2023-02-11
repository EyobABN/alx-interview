#!/usr/bin/python3
""" Module for Pascal's triangle """


def pascal_triangle(n):
    """ Function for Pascal's triangle """
    if (n <= 0):
        return []
    t = []
    for i in range(n):
        r = [1]
        for j in range(i):
            r.append(1)
        t.append(r)
    return t
