#Problem 3: What is the largest prime factor of the number 600851475143 ?

def next_prime(prime):
    ''' (int) -> int

    Return the next prime number

    next_prime(13) -> 17
    next_prime(31) -> 37'''
    next = prime + 1

    while True:
        for i in range(2,next+1):
            if i == next:
                return next
            elif next%i == 0:
                break
        next = next + 1

def largestfactor (number):
    ''' (int) -> int

    Return the largest prime factor of a number.

    largestfactor(13195) -> 29
    largest factor (600851475143) -> 6857

'''

    factors = []
    prime = 2

    while True:
        if number % prime == 0 and number != 1:
            number = number / prime
            if prime not in factors:
                factors.append(prime)
        elif number == 1:
            return max(factors)
        else:
            prime = next_prime(prime)
