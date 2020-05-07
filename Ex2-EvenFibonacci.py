def fibonacci(maximo):
    ''' (int) -> list

        Return the Fibonacci sequence with the maximum value given by maximo.

        fibonacci(89) -> [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
        '''

        fibonacci = [1,2]

        while fibonacci[-1] <= maximo:
            fibonacci.append(fibonacci[-1]+fibonacci[-2])

        return fibonacci
        
def sum_even(x):
    ''' (list) -> int

    Return the sum of even numbers in a list

    sum_even([1, 2, 3, 5, 8, 13, 21, 34, 55, 89]) -> 44
    '''
    even
