def fibonacci(maximo):
    ''' (int) -> list

        Return the Fibonacci sequence with the maximum value given by maximo.

        fibonacci(89) -> [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        '''

    fibo = [1,2]

    while fibo[-1] <= maximo:
        fibo.append(fibo[-1]+fibo[-2])

    return fibo

def sum_even(maximo):
    ''' (list) -> int

    Return the sum of even numbers in a list

    sum_even([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) -> 44
    '''

    total = 0

    for i in fibonacci(maximo):
        if i%2 == 0:
            total = total + i

    return total
