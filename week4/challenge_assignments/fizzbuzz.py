
def eval_fizzbuzz(n: int) -> str | int: 
    # TODO: 
    if not n % 3 and not n % 5: 
        return "FizzBuzz"

    if not n % 3: 
        return "Fizz"
    
    if not n % 5: 
        return "Buzz"

    return str(n)
    # if n is divisible by 3, return "Fizz"
    # if n is divisible by 5, return "Buzz"
    # if n is divisible by 3 and 5, return "FizzBuzz"
    # else, return n

    return n


