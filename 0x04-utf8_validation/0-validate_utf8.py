#!/usr/bin/python3
'''UTF-8 Validation'''


from typing import List


def get_byte_value(number: int) -> bytes:
    '''
    return the byte representation of an integer
    an integer can have from 1 to 4 bytes
    '''

    # before division i added 7 to always get a number >= 8
    # (//) means that i get the floor of the division,
    # like ( 5 // 2 = 2 NOT 2.5 )
    # example: 3 => 0b11, ==> 2 + 7 = 9, ==> 9 // 8 = 1

    num_bytes = (number.bit_length() + 7) // 8

    # get the byte representation of an integer
    byte_value = number.to_bytes(num_bytes, 'big')
    return byte_value


def validUTF8(data: List[int]) -> bool:
    '''validating if a set of data is a valid utf-8'''
    if not data or data == []:
        return False

    # a dict {length of bytes : (mask, expected result for '&' operation)}
    masks = {
        2: (0b11100000, 0b11000000),
        3: (0b11110000, 0b11100000),
        4: (0b11111000, 0b11110000),
    }
    # the mask of the rest of the byte when len > 1, and result of '&'
    mask_rest = (0b11000000, 0b10000000)

    for number in data:

        if not isinstance(number, int):
            return False

        byte_value = get_byte_value(number)
        bytes_len = len(byte_value)

        # if 1 byte and valid
        if bytes_len == 1 and byte_value[0] & 0b10000000 == 0:
            continue

        elif 1 < bytes_len <= 4:

            # check if most significant byte is valid
            if byte_value[0] & masks[bytes_len][0] != masks[bytes_len][1]:
                return False

            # check if rest of bytes are valid
            i = 0
            while i < bytes_len - 1:
                if byte_value[i] & mask_rest[0] != mask_rest[1]:
                    return False

                i += 1

        else:
            return False

    return True
