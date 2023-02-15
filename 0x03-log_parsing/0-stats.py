#!/usr/bin/python3
""" Module for Log Parser """

import sys

if (__name__ == "__main__"):
    counter = 0
    total_size = 0
    codes = {}
    for line in sys.stdin:
        date_sep = line.split(' - [')
        ip = date_sep[0]
        date_rest = date_sep[1].split('] "')
        date = date_rest[0]
        get_rest = date_rest[1].split('"')
        get = get_rest[0]
        sc_fs = get_rest[1].split()
        sc = sc_fs[0]
        fs = sc_fs[1]
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
