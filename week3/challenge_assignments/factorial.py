from utils import input_int

def comp_factorial(x: int) -> int:
    """
        function for computing the factorial of some number x
    """

    # if it's not an int, return
    if type(x) != int:
        print(f"error, type {type(x)} unsupported for factorial operation")
        return -1

    # now, loop from 1 to x
    for i in range(1, x): 
        x *= i

    return x


# this should print a warning
error_case = comp_factorial("laksjdf")

# this should print 2
fac_2 = comp_factorial(2)
print(fac_2)

# this should print 40320
fac_8 = comp_factorial(8)
print(fac_8)

# this should print 479001600
fac_12 = comp_factorial(12)
print(fac_12)

# this is number of card permutations in a 52 card deck
num_decks = comp_factorial(52)
print(f"in a 52 card deck, there are {num_decks} possible decks")

# now, loop user input until -1
num = 0
while (num != -1): 
    num = input_int("input a number greater than 0, enter -1 to quit")
    num_fact = comp_factorial(num)
    print(num_fact)

