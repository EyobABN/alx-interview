#!/usr/bin/python3
""" Module for Log Parser """


# import signal
import sys
import ipaddress


def is_ipv4(string):
    try:
        ipaddress.IPv4Network(string)
        return True
    except ValueError:
        return False


def is_get(string):
    if (string == "GET /projects/260 HTTP/1.1"):
        return True
    return False


def is_code(string):
    if (int(string) in [200, 301, 400, 401, 403, 404, 405, 500]):
        return True
    return False


def is_size(string):
    return string.isdigit()


# def handler(signum, frame):
#     print("File size: {}".format(total_size))
#     for code in sorted(codes.keys()):
#         print("{}: {}".format(code, codes[code]))
#     raise KeyboardInterrupt


# signal.signal(signal.SIGINT, handler)

if (__name__ == "__main__"):
    counter = 0
    total_size = 0
    codes = {}

    try:
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
            if (is_ipv4(ip) is False or
                    is_get(get) is False or
                    is_code(sc) is False or
                    is_size(fs) is False):
                continue
            total_size += int(fs)
            if sc in codes:
                codes[sc] += 1
            else:
                codes[sc] = 1
            counter += 1
            if (counter % 10 == 0):
                print("File size: {}".format(total_size))
                for code in sorted(codes.keys()):
                    print("{}: {}".format(code, codes[code]))
    except KeyboardInterrupt:
        print("File size: {}".format(total_size))
        for code in sorted(codes.keys()):
            print("{}: {}".format(code, codes[code]))
