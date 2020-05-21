#Problem 6: Find the difference between the sum of the squares of the first one
#hundred natural numbers and the square of the sum.

def sum_square_dif (x,y):
    '''(int), (int) -> int

    Return the difference between the sum of the squares of two natural numbers
    (x,y) and the square of the sum.

    sum_square_dif (1,10) -> 2640
    '''

    sum_squares = 0
    square_sum = 0

    for i in range(x,y)
        sum_squares = sum_squares + i**2
        square_sum = square_sum + i

    return (square_sum**2)-sum_squares
