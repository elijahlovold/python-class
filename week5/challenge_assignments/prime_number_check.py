"""
Description: Determine whether a given integer is a prime number.
Input Arguments:
n (int): The number to check for primality.
"""
from math import sqrt

def is_prime(n): 
    if n < 2: 
        return False

    if n == 2: 
        return True

    if n % 2 == 0: 
        return False

    # only need to check up to sqrt n 
    # also, since we checked 2, iterate by two to skip all evens
    for i in range(3, int(sqrt(n)), 2): 
        if n % i == 0: 
            return False

    return True

