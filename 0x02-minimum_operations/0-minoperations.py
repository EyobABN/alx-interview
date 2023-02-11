#!/usr/bin/python3
""" module for a minOperations function """


def smallestFactor(n):
    """ returns the smallest prime number that can divide the number n """
    for i in range(2, int(n+1)):
        if (n % i == 0):
            return i


def minOperations(n):
    """ returns the minimum number of operations """
    sF = smallestFactor(n)
    if sF == n:
        return 0

    ops = 0
    while (n > 1):
        sF = smallestFactor(n)
        ops = ops + sF
        n = n / sF

    return ops
