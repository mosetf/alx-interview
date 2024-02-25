
#!/usr/bin/python3
"""
UTF-8 validation module.
"""


def validUTF8(data):
    """
    Function that checks if a list of integers are valid UTF-8 codepoints.
    See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
    """
    skip = 0
    m = len(data)
    for j in range(m):
        if skip > 0:
            skip -= 1
            continue
        if type(data[j]) != int or data[j] < 0 or data[j] > 0x10ffff:
            return False
        elif data[j] <= 0x7f:
            skip = 0
        elif data[j] & 0b11111000 == 0b11110000:
            # 4-byte utf-8 character encoding
            span = 4
            if m - j >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[j + 1: j + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[j] & 0b11110000 == 0b11100000:
            # 3-byte utf-8 character encoding
            span = 3
            if m - j >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[j + 1: j + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        elif data[j] & 0b11100000 == 0b11000000:
            # 2-byte utf-8 character encoding
            span = 2
            if m - j >= span:
                next_body = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[j + 1: j + span],
                ))
                if not all(next_body):
                    return False
                skip = span - 1
            else:
                return False
        else:
            return False
    return True
