import random
from util import wait_for_user_start

# Game 2: Dungeon Escape
def play_dungeon_escape(): 
    while True: 
        if not wait_for_user_start(): 
            break

        print("\nYou've entered the dungeon...")
        
        player_won = False
        while True: 
            choice = input("You come to two hallways, chose left or right (l/r): ").lower()

            if choice in ["l", "left"]: 
                choice = input("You confront a monster, fight or run (f/r): ").lower()
                if choice in ["f", "fight"]: 
                    win = bool(random.randint(0, 1)) 
                    if win: 
                        print("You killed the monster!")
                        player_won = True
                    else: 
                        print("You died")
                    break
            else: 
                player_won = True
                break

        if player_won: 
            print("Congratulations! You've escaped the dungeon")

if __name__ == "__main__": 
    play_dungeon_escape()
