#!/usr/bin/python3
""" Log parsing """
import sys
import re


status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
file_size = 0
count = 0

def print_stats(status_codes, file_size):
    """ Method that prints the log parsing stats """
    print("File size: {:d}".format(file_size))
    for key in sorted(status_codes.keys()):
        print("{:s}: {:d}".format(key, status_codes[key]))

pattern = re.compile(r'(?P<ip>[\d\.]+) - \[(?P<date>.*?)\] "(?P<request>.*?)" (?P<status>\d+) (?P<size>\d+)')

if __name__ == "__main__":

    try:
        for line in sys.stdin:
            count += 1
            match = pattern.match(line)

            if match:
                status = match.group("status")
                file_size += int(match.group("size"))
                if status in status_codes:
                    status_codes[status] += 1
            if count % 10 == 0:
                print_stats(status_codes, file_size)
    except KeyboardInterrupt:
        print_stats(status_codes, file_size)
        raise
    print_stats(status_codes, file_size)
