'Problem 3: What is the largest prime factor of the number 600851475143 ?'

def primes (number):
    ''' (int) -> list

    Return a list with all primes lower than number

    primes(15) -> [2,3,5,7,11,13]'''
def prime_factors(number):
    ''' (int) -> list

    Return a list with the prime factors of a number

    primes(13195) -> [5,7,13,29]'''

    factors = []
    primes = [2,3,5,7]
    for i in range (2,number):
        if i %
