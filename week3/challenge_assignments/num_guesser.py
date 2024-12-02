from random import randint
from utils import input_int

max_num = 0
min_num = 0

valid_range = False
while not valid_range: 
    max_num = input_int("max number")
    min_num = input_int("min number")

    valid_range = max_num > min_num
    if not valid_range:
        print(f"error, min ({min_num}) must be >= max ({max_num})")
    
# use the randint function to generate a random int between the limits
rand_number = randint(min_num, max_num)

# loop until they find it
while True: 
    user_guess = input_int("guess number: ")

    if user_guess == rand_number: 
        print("correct!")
        break

    if user_guess < rand_number: 
        print("higher")

    if user_guess > rand_number: 
        print("lower")

