#Problem 4: Find the largest palindrome made from the product of two 3-digit numbers.

def largest(digits):
    ''' (int) -> int

    return the largest palindrome from the product of the numbers with
    the given number of digits

    palindrome(2) -> 9009 '''

    first = 10**(digits-1)
    last = (10**digits)-1

    palindrome = [0]

    for i in range(last, first, -1):
        for x in range(last, first, -1):
            product = i * x
            if str(product) == str(product)[::-1] and palindrome[0] < product:
                palindrome[0] = product

    return palindrome[0]
