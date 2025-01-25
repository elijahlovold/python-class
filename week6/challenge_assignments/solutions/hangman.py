import random
from util import wait_for_user_start

# Game 1: Hangman
def play_hangman(): 
    while True: 
        if not wait_for_user_start(): 
            break

        print("\nTry not to die")

if __name__ == "__main__": 
    play_hangman()
