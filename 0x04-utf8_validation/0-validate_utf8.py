#!/usr/bin/python3
'''UTF-8 Validation'''


from typing import List


def validUTF8(data: List[int]) -> bool:
    '''validating if a set of data is a valid utf-8'''

    for number in data:

        bin_number = f'{number:08b}'
        len_bits = len(bin_number)

        if len_bits == 8:
            msb = bin_number[0]
            return True if msb == 0 else False

        if len_bits > 8:
            # print(len(bin_number))
            # get the two most significant bites of the last 8 bits
            two_msb = bin_number[-8:-6]

            if two_msb != "10":
                return False

    return True
