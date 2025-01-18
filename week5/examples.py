
def prog_breaker(iteration): 
    print(iteration)
    prog_breaker(iteration+1)

# this will print 0, 1, 2, etc. until it crashes
prog_breaker(0)

