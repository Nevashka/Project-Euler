def multiples(top):
    '''(int) -> int

    Return the sum of all multiples of 3 and 5 bellow the chosen number.

    multiples(10) -> 23
    multiples(100) -> 2318
    '''
    total = 0
    for i in range(1,top):
        if i%3 == 0 or i%5 == 0:
            total = total + i

    return total
