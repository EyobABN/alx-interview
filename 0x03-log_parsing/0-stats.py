#!/usr/bin/python3
""" Module for Log Parser """


import signal
import sys
import os


"""
import ipaddress


def is_ipv4(string):
    try:
        ipaddress.IPv4Network(string)
        return True
    except ValueError:
        return False
        """


def handler(signum, frame):
    print(f"File size: {total_size}")

    """ print sorted codes """
    for code in sorted(codes.keys()):
        print(f"{code}: {codes[code]}")
    raise KeyboardInterrupt


signal.signal(signal.SIGINT, handler)

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

    """ increment total_size """
    total_size += int(fs)

    """ update codes with new status code """
    if sc in codes:
        codes[sc] += 1
    else:
        codes[sc] = 1

    """ increment counter and print stats on every 10th or on Ctrl-C """
    counter += 1
    if (counter % 10 == 0):
        print(f"File size: {total_size}")

        """ print sorted codes """
        for code in sorted(codes.keys()):
            print(f"{code}: {codes[code]}")
