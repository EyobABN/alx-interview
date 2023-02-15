#!/usr/bin/python3
""" Module for Log Parser """

import sys

if (__name__ == "__main__"):
    counter = 0
    total_size = 0
    codes = {}
    for line in sys.stdin:
        total_size += int(fs)
        if sc in codes:
            codes[sc] += 1
        else:
            codes[sc] = 1
        counter += 1
        if (counter % 10 == 0):
            print(f"File size: {total_size}")
            for code in sorted(codes.keys()):
                print(f"{code}: {codes[code]}")
