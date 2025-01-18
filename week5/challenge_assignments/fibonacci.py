"""
Description: Compute the nth Fibonacci number in the Fibonacci sequence using recursion or looping
Input Arguments:

n (int): The position in the Fibonacci sequence (0-indexed).
"""

# recursive solution...
def recurse_fibo(current, next, i, n): 
    if n == 0: 
        return 0

    if i >= n: 
        return current
    
    return recurse_fibo(next, current+next, i+1, n)

def fibonacci(n): 
    return recurse_fibo(0, 1, 0, n)


# ...or list solution
# def fibonacci(n): 
#     if n == 0: 
#         return 0

#     vals = [0,1]
#     while len(vals) < n+1: 
#         vals.append(vals[-1] + vals[-2])

#     return vals[-1]
# print(fibonacci(1))
