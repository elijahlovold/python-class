def prog_breaker(iteration): 
    print(iteration)

    if (iteration > 3): 
        return

    prog_breaker(iteration+1)


# this will print 0, 1, 2, etc. until it crashes
prog_breaker(0)

# import matplotlib.pyplot as plt
# from test_functions import foo

# plt.plot([1,2,3])
# plt.show()

# print(foo)

def compute_max(x, init_max=-9999) -> int: 
    max = init_max

    for i in x: 
        if i > max: 
            max = i
    return max

def compute_min(x) -> int: 
    min = 9999

    for i in x: 
        if i < min: 
            min = i
    return min

def compute_total(x) -> int: 
    total = 0
    for i in x: 
        total += i

    return total

def compute_stats(some_list): 
    print(some_list)

    # compute max
    max = compute_max(some_list)

    # compute min
    min = compute_min(some_list)

    # compute total
    total = compute_total(some_list)

    print("max was: ", max)
    print("min was: ", min)
    print("total was: ", total)

    return max + min / total

num = [1,2,3]
foo = compute_stats(num)


# create a function to compute some stats




