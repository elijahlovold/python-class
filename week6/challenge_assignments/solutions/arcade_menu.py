# import game functions from other files...
from dungeon_escape import play_dungeon_escape
from word_scramble import play_scramble

# Menu to play the games
while True:
    print("\nChoose a game:")
    print("1. Hangman")
    print("2. Dungeon Escape")
    print("3. Word Scramble")
    print("4. Quit")

    game_select = input().lower()

    if game_select in ["1", "h", "hangman"]: 
        print("sorry, this game is not yet supported")

    elif game_select in ["2", "d", "dungeon"]: 
        play_dungeon_escape()

    elif game_select in ["3", "s", "scramble"]: 
        play_scramble()

    elif game_select in ["4", "q", "quit"]: 
        break
