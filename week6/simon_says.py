from random import randint
from os import system
from time import sleep

# objective: create the game simon says (the one with colors)

def grab_valid_input(message: str, max_symbol: int=9) -> int: 
    while True: 
        user_input = int(input(message))

        if user_input > 1 and user_input <= max_symbol: 
            return user_input
        else: 
            print(f"invalid, enter between 2 and {max_symbol}")


def wait_for_player_start() -> int: 
    """Waits for player start, inditicating number of symbols"""

    return grab_valid_input("Enter number of symbols to start: ")

def add_new_element(grid: list, max_symbol: int) -> list: 
    """append a new random item onto the grid."""
    # somehow generate a random symbol
    rand_num = randint(2, max_symbol)

    random_symbol = str(rand_num)

    grid += [random_symbol]

    # not necessary
    return grid
    
def display_grid(grid: list, display_time: float=0.8): 
    # clear display
    system("clear")

    # loop through the grid 
    for i in grid: 
        # display ith element
        print(i) 
        sleep(display_time)

        # clear display
        system("clear")
        sleep(display_time)

def input_user_sequence(grid, max_symbol) -> bool: 
    """Returns """

    for i in grid: 
        # input a VALID user input
        user_input = grab_valid_input("", max_symbol)

        # check to see if it matches i
        if str(user_input) != i: 
            return False

        # clear 
        system("clear")

    return True

def play_simon_says(): 
    # runs the entire time
    while True: 
        # wait for player to start
        max_symbol = wait_for_player_start()

        # init
        grid = []
            
        round = 1

        game_played = True
        while game_played: 
            print("Round: ", round)
            sleep(1)

            # append a new RANDOM element to grid
            grid = add_new_element(grid, max_symbol)

            # display the sequence
            display_grid(grid)

            # input the sequence while checking each element 
            game_played = input_user_sequence(grid, max_symbol)
        
            sleep(0.8)
            round += 1

        print("you lose, again")

if __name__ == "__main__":
    print("running simon says")
    play_simon_says()

