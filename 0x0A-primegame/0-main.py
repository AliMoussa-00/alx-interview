#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

sieve_of_Eratosthenes = __import__('0-prime_game').sieve_of_Eratosthenes


# print(f'primes = ${sieve_of_Eratosthenes(11)}')

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(5, [10])))
print("Winner: {}".format(isWinner(5, [11])))
