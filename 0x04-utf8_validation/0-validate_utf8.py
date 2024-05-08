#!/usr/bin/python3
'''UTF-8 Validation'''


from typing import List


def validUTF8(data: List[int]) -> bool:
    '''validating if a set of data is a valid utf-8'''

    for number in data:

        # Define a binary string
        binary_string = f'{number:08b}'

        # Valid UTF-8 ranges for the first byte of a character
        valid_ranges = [
            (0x00, 0x7F),  # Single-byte characters (ASCII)
            (0xC2, 0xDF),  # Two-byte characters
            (0xE0, 0xEF),  # Three-byte characters
            (0xF0, 0xF4)   # Four-byte characters
        ]

        # Check if byte falls within any of the valid ranges
        for start, end in valid_ranges:
            if start <= number <= end:
                return True

        return False
