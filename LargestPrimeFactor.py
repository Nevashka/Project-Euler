#Problem 3: What is the largest prime factor of the number 600851475143 ?

def total_primes(number):
    ''' (int) -> list

    Return a list with all primes lower than number.

    primes(15) -> [2,3,5,7,11,13]
    primes(30) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    '''

    all_primes = [2,3,5,7,11,13,17,19]
    maximo = 19

    while maximo < number:
        maximo = maximo + 1
        for i in range(2,number):
            if maximo % i == 0 and i != maximo:
                break
            elif i == maximo:
                all_primes.append(maximo)
                break

    return all_primes

def primefactors (number):
    ''' (int) -> int

    Return the largest prime factor of a number.

    primes(13195) -> 29
'''

    factors = []
    primes = total_primes(number)

    for i in primes:
        if number % i == 0:
            factors.append(i)
            while number % i == 0:
                number = number / i

    return max(factors)
