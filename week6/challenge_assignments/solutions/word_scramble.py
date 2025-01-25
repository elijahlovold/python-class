import random
from util import wait_for_user_start

# Game 3: Word Scramble
def play_scramble(): 
    list_of_options = ["skiing", "python", "pizza", "scramble"]

    while True: 
        if not wait_for_user_start(): 
            break

        word = random.choice(list_of_options)
        scrambled_word = random.sample(word, len(word))

        print("\nScrambled Word: ", scrambled_word)
        while True: 
            guess = input("Unscrambled Word: ")
            if guess == word: 
                break

            print("WRONG!")

        print("correct")

if __name__ == "__main__": 
    play_scramble()
