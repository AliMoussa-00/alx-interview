#!/usr/bin/python3
'''Minimum Operations'''

import math


# def minOperations(n: int) -> int:
#     '''
#     Calculates the sum of prime factors of a given positive integer "n"
#     Time Complexity:  O(sqrt(n))
#     '''
#     if n <= 0 or not isinstance(n, int):
#         return 0

#     total = 0
#     factor = 2
#     sqrt_n = int(math.sqrt(n))

#     while factor <= sqrt_n:
#         if n <= 1:
#             break

#         if n % factor == 0:
#             total += factor

#             n //= factor
#             continue

#         factor += 1

#     return total
def minOperations(n: int) -> int:
    '''
    Calculates the sum of prime factors of a given positive integer "n"
    Time Complexity:  O(sqrt(n))
    '''
    if n <= 1:
        return 0

    dp = [0] * (n + 1)
    for i in range(2, n + 1):
        dp[i] = float('inf')
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    return int(dp[n])
