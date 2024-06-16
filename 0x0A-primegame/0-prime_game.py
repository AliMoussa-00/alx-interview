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

    # let just return the list of prime number less or equal n in nums

    is_Maria = True
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        i = 0
        primes = sieve_of_Eratosthenes(n)
        while i < x and len(primes) > 0:
            primes.pop(0)
            is_Maria = not is_Maria
            i += 1

        if is_Maria:
            ben_wins += 1
        else:
            maria_wins += 1

    winner = 'Maria' if maria_wins > ben_wins else 'Ben'
    return winner
