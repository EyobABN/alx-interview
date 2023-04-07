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


# def isWinner(x, nums):
#     """Prime Game function"""
#     if x < 1 or not nums:
#         return None
#     p1 = 'Maria'
#     p2 = 'Ben'
#     p1_score = 0
#     p2_score = 0

#     # make a list of all prime numbers up to the max value in nums
#     n = max(nums)
#     primes = [True for _ in range(1, n + 1)]
#     primes[0] = False
#     for i, is_prime in enumerate(primes, 1):
#         if i == 1 or not is_prime:
#             continue
#         for j in range(i * i, n + 1, i):
#             primes[j - 1] = False
#     # start game
#     for _, n in zip(range(x), nums):
#         # primes = list(filter(lambda x: x, primes[0: n]))
#         primes = list(filter(lambda x: x, primes[0: n]))
#         if len(primes) % 2 == 0:
#             p2_score += 1
#         else:
#             p1_score += 1

#     if p1_score > p2_score:
#         return p1
#     elif p1_score == p2_score:
#         return None
#     return p2

def isWinner(x, nums):
    """Prime Game function"""
    if x < 1 or not nums:
        return None
    p1 = 'Maria'
    p2 = 'Ben'
    p1_score = 0
    p2_score = 0

    # make a list of all prime numbers up to the max value in nums
    n = max(nums)
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # pre-calculate the number of primes up to each value in nums
    prime_counts = [0] * (n + 1)
    for i in range(2, n + 1):
        prime_counts[i] = prime_counts[i - 1] + primes[i]

    # start game
    for _, n in zip(range(x), nums):
        primes_count = prime_counts[n]
        if primes_count % 2 == 0:
            p2_score += 1
        else:
            p1_score += 1

    if p1_score > p2_score:
        return p1
    elif p1_score == p2_score:
        return None
    return p2
