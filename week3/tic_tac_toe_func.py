def input_min_number(min_value: int, message: str): 
    while (True): 
        in_str = input(f"{message} (>= {min_value}): ")
        try: 
            value = int(in_str)
            if (value >= min_value): 
                return value
        except:
            pass
        print("invalid input")

def print_grid(grid: list): 
    for row in grid: 
        r_str = '' 
        for col in row: 
            r_str += col + ' '
        print(r_str, '\n')

def input_coords(grid: list, sym: str): 
    N = len(grid)
    valid = False
    while (not valid): 
        in_str = input(f"player {sym}: give two coordinates: ")
        try: 
            x, y = in_str.split(" ")
            x = int(x)
            y = int(y)
            if (x < 1 or N < x or y < 1 or N < y): 
                print("invalid coords")
            else: 
                # convert to 0-based index
                x -= 1
                y -= 1
                if (grid[y][x] != '-'): 
                    print("invalid, player already placed here")
                else: 
                    grid[y][x] = sym 
                    valid = True
        except:
            print("error input")
            continue

def check_player_win(grid: list, sym: str) -> bool: 
    N = len(grid)

    # check if user1 wins
    straight_won = False
    diag_won = True
    diag_r_won = True
    grid_full = True
    for i in range(N): 
        row_won = True
        col_won = True
        for j in range(N): 
            if (grid[i][j] != sym): 
                row_won = False
            if (grid[j][i] != sym): 
                col_won = False

            # if at least one symbol in the grid is an empty char, 
                # it is not full
            if (grid[i][j] == '-'): 
                grid_full = False

        if (row_won or col_won):
            straight_won = True
            break

        if (grid[i][i] != sym): 
            diag_won = False
        if (grid[N - 1 - i][i] != sym): 
            diag_r_won = False

    if straight_won or diag_won or diag_r_won: 
        print(f"player {sym} won!")
        return True

    # check for tie
    elif (grid_full == True): 
        print("tie")
        return True

    return False

# let size of grid be N
N = input_min_number(3, "input grid size")

# number of players be P
P = input_min_number(2, "input number of players")

# load in player symbols
player_symbols = ['']*P
for i in range(P): 
    symb = input(f"input player {i} symbol: ")
    player_symbols[i] = symb

# create a list to represent the grid
grid = []
for _ in range(N): 
    row = []
    for _ in range(N): 
        row.append('-')
    grid.append(row)
print_grid(grid)

# while loop for playing the game
game_over = False
while (not game_over): 

    for sym in player_symbols:
        input_coords(grid, sym)
        print_grid(grid)

        game_over = check_player_win(grid, sym)
        if game_over:
            break

