#Problem 5: What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def smallest_multiple(x,y):
    '''(int), (int) -> int

    Return the smallest number that can be divised by each numbers from x to y
    without any remainder.

    smallest_multiple(1,10) -> 2520
    '''
    multiple = y*2

    while True:
        for i in range(x,y+1):
            if multiple % i != 0:
                break
            elif i == y:
                return multiple
        multiple = multiple + y
