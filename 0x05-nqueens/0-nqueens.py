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
    print(sys.argv[1])
