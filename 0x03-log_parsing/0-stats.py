#!/usr/bin/python3
'''
Module Docs
'''
import sys
from typing import Dict


def print_summary(total_file_size: int, status_counts: Dict[str, int]) -> None:
    """
    Print the total file size and counts of HTTP status codes.

    :param total_file_size: Total file size accumulated so far.
    :param status_counts: Dictionary containing counts of different HTTP status
    codes.
    """
    print("File size: {:d}".format(total_file_size))
    for code, count in sorted(status_counts.items()):
        if count != 0:
            print("{} : {}".format(code, count))


# Dictionary to store counts of different HTTP status codes
http_status_counts: Dict[str, int] = {'200': 0, '301': 0, '400': 0, '401': 0,
                                      '403': 0, '404': 0, '405': 0, '500': 0}

# Initialize variables
total_file_size: int = 0
line_count: int = 0


try:
    # Iterate over lines from standard input
    for line in sys.stdin:
        # Split the line into words
        line_args = line.split()

        if len(line_args) > 2:
            # Extract HTTP status code and file size
            status_code: str = line_args[-2]
            file_size: int = int(line_args[-1])

            # Update counts in the dictionary
            if status_code in http_status_counts:
                http_status_counts[status_code] += 1

            # Update total file size and line count
            total_file_size += file_size
            line_count += 1

            # Print summary every 10 lines
            if line_count == 10:
                print_summary(total_file_size, http_status_counts)
                line_count = 0

except KeyboardInterrupt:
    pass

finally:
    # Print final summary
    print_summary(total_file_size, http_status_counts)