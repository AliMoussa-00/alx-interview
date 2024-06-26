#!/usr/bin/python3
'''Prime Game'''


def sieve_of_Eratosthenes(n):
    '''
    return a list of prime number less or equal n
    using : Sieve of Eratosthenes Algorithm
    '''

    primes = [True for i in range(n + 1)]
    primes[0] = primes[1] = False
    p = 2

    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False

        p += 1

    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    '''who is the winner, Maria or Ben ? '''
    if x is None or nums is None or x == 0 or nums == []:
        return None

    if x > len(nums):
        return None

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        primes = sieve_of_Eratosthenes(nums[i])
        if not primes or len(primes) == 0:
            ben_wins += 1
            continue

        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
