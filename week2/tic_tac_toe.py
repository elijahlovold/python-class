# let size of grid be N
while (True): 
    in_str = input("input grid size (> 2): ")
    try: 
        N = int(in_str)
        if (N > 2): 
            break
    except:
        pass
    print("invalid input")

# create a list to represent the grid
grid = []
for _ in range(N): 
    row = []
    for _ in range(N): 
        row.append('-')
    grid.append(row)

# row1 = ['-', '-', '-']
# row2 = ['-', '-', '-']
# row3 = ['-', '-', '-']

# grid = [row1, row2, row3]

# select_row = grid[0]
# select_row[1] = 'O'

# grid[0][1] = 'O'

# print the grid 
for row in grid: 
    r_str = '' 
    for col in row: 
        r_str += col + ' '
    print(r_str, '\n')

# while loop for playing the game
while (True): 

    # while loop to get user1 input 
    # store 'O' at the grid location user input
    valid = False
    while (not valid): 
        in_str = input("player 1: give two coordinates: ")
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
                    grid[y][x] = 'O'
                    valid = True
        except:
            print("error input")
            continue

    # print the grid 
    for row in grid: 
        r_str = '' 
        for col in row: 
            r_str += col + ' '
        print(r_str, '\n')

    # check if user1 wins
    straight_won = False
    diag_won = True
    diag_r_won = True
    grid_full = True
    for i in range(N): 
        row_won = True
        col_won = True
        for j in range(N): 
            if (grid[i][j] != 'O'): 
                row_won = False
            if (grid[j][i] != 'O'): 
                col_won = False

            # if at least one symbol in the grid is an empty char, 
                # it is not full
            if (grid[i][j] == '-'): 
                grid_full = False

        if (row_won or col_won):
            straight_won = True
            break

        if (grid[i][i] != 'O'): 
            diag_won = False
        if (grid[N - 1 - i][i] != 'O'): 
            diag_r_won = False

    if straight_won or diag_won or diag_r_won: 
        print("player 1 won!")
        break

    # check for tie
    elif (grid_full == True): 
        print("tie")
        break

    # -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~
    # -~ Note, everything after this is nearly identical -~--~-~-~-~
    # -~ Just using player 2 and checking for a different symbol -~-
    # -~ Keep this in mind when we introduce functions... -~-~-~-~-~
    # -~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~

    # while loop to get user2 input 
    # store 'X' at the grid location user input
    valid = False
    while (not valid): 
        in_str = input("player 2: give two coordinates: ")
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
                grid[y][x] = 'X'
                valid = True

    # print the grid 
    for row in grid: 
        r_str = '' 
        for col in row: 
            r_str += col + ' '
        print(r_str, '\n')

    # check if user2 wins
    straight_won = False
    diag_won = True
    diag_r_won = True
    grid_full = True
    for i in range(N): 
        row_won = True
        col_won = True
        for j in range(N): 
            if (grid[i][j] != 'X'): 
                row_won = False
            if (grid[j][i] != 'X'): 
                col_won = False

            # if at least one symbol in the grid is an empty char, 
                # it is not full
            if (grid[i][j] == '-'): 
                grid_full = False

        if (row_won or col_won):
            straight_won = True
            break

        if (grid[i][i] != 'X'): 
            diag_won = False
        if (grid[N - 1 - i][i] != 'X'): 
            diag_r_won = False

    if straight_won or diag_won or diag_r_won: 
        print("player 2 won!")
        break

    # check for tie
    elif (grid_full == True): 
        print("tie")
        break

