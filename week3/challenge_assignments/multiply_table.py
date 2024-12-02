from utils import input_int

def print_basic_ugly_multiply_table(N: int) -> None:
    for i in range(1, N+1): # vertical
        row_str = ""
        for j in range(1, N+1): # horizontal
            row_str += str(i*j) + " "

        print(row_str)

def print_square_multiply_table(N: int) -> None:
    # this is the len of the max number that will appear
    max_str_len = len(str(N*N))

    for i in range(1, N+1): # vertical
        row_str = ""
        for j in range(1, N+1): # horizontal
            number = str(i*j)
            if len(number) < max_str_len:
                # computer how many chars short the str is
                len_diff = max_str_len - len(number)

                # create a padding of spaces equal to the number of missing chars
                space_padding = " "*len_diff

                
                # add that many spaces in front of the number
                number = space_padding + number

            row_str += number + " "

        print(row_str)

num = input_int("enter a number to print a multiplication table up to")

print("\nbasic version: ")
print_basic_ugly_multiply_table(num)

print("\nbetter version: ")
print_square_multiply_table(num)

