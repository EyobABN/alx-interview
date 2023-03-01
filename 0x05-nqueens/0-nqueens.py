#!/usr/bin/python3
"""
N Queens module
"""

import sys


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
    if (not N.isdigit()):
        print("N must be a number")
        exit(1)
    N = int(N)
    if (N < 4):
        print("N must be at least 4")
        exit(1)

    def queens(n, i, a, b, c):
        """
        Translation of Niklaus Wirth's solution into Python
        source: https://en.wikipedia.org/wiki/Eight_queens_puzzle
        """
        if i < n:
            for j in range(n):
                if j not in a and i+j not in b and i-j not in c:
                    yield from queens(n, i+1, a+[j], b+[i+j], c+[i-j])
        else:
            yield a

    for solution in queens(N, 0, [], [], []):
        for idx, y in enumerate(solution):
            solution[idx] = [idx, y]
        print(solution)
