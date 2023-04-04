#!/usr/bin/python3
"""Module for Prime Game algorithm"""


def get_primes(n):
    """Returns a list of prime numbers up to and including n"""
    primes = []
    for num in range(2, n+1):
        is_prime = True
        for i in range(2, int(num**(0.5))+1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes


def isWinner(x, nums):
    """Prime Game function"""
    if not isinstance(x, int):
        raise TypeError('First argument must be an integer')
    if not isinstance(nums, list) or not all(isinstance(i, int) for i in nums):
        raise TypeError('Second Argument must be a list of integers')
    p1 = 'Maria'
    p2 = 'Ben'
    p1_score = 0
    p2_score = 0

    for n in nums:
        primes = get_primes(n)
        if len(primes) == 0 or len(primes) % 2 == 0:
            p2_score += 1
        else:
            p1_score += 1

    # print('Maria : {}'.format(p1_score))
    # print('Ben   : {}'.format(p2_score))

    if p1_score > p2_score:
        return p1
    return p2