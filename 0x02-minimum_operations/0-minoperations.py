#!/usr/bin/python3
'''Minimum Operations'''

import math


def minOperations(n: int) -> int:
    '''
    Calculates the sum of prime factors of a given positive integer "n"
    Time Complexity:  O(sqrt(n))
    '''
    if n <= 0 or not isinstance(n, int):
        return 0

    total = 0
    factor = 2
    sqrt_n = int(math.sqrt(n))

    while factor <= sqrt_n:
        if n <= 1:
            break

        if n % factor == 0:
            total += factor

            n //= factor
            factor = 2
            continue

        factor += 1

    if n > 1:
        factor += n

    return total
