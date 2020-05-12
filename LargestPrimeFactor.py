#Problem 3: What is the largest prime factor of the number 600851475143 ?

def total_primes(number):
    ''' (int) -> list

    Return a list with all primes lower than number.

    primes(15) -> [2,3,5,7,11,13]
    primes(30) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    '''

    all_primes = [2,3,5,7,11,13,17,19]
    maximo = 19

    while maximo < maximo + 1:
        maximo = maximo + 1
        for i in range(2,number):
            if maximo % i == 0 and i != maximo:
                break
            elif i == maximo:
                all_primes.append(maximo)
                break

    return all_primes

def next_prime(next):
    ''' (int) -> int

    Return the next prime number

    next_prime(13) -> 17
    next_prime(31) -> 37'''

    while True:
        next = next + 1
        for i in range(1,next+1):
            if next%i == 0 and i!=next:
                break
            elif i == next:
                return next


def primefactors (number):
    ''' (int) -> int

    Return the largest prime factor of a number.

    primes(13195) -> 29
'''

    factors = []
    prime = 2

    while True:
        if number % prime == 0 and number != 1:
            number = number / prime
            if prime not in factors:
                factor.append(prime)
        elif number == 1:
            return max(factors)
        else:
            prime = next_prime(prime)
