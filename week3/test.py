
def print_hello_world(): 
    # some message 
    print("hello world")

def print_some_message(message): 
    print(message)

    print("this was from a funtion")


    # \, *args, **kwargs, = 
def input_num(message, max_num_attempts=999999): 
    i = 0
    while (i < max_num_attempts): 
        input_str = input(message)

        try: 
            input_num = int(input_str)
            return input_num
        except:
            print("please enter a valid int")
            i += 1


# print_some_message("hello world from the outside!")

# print_hello_world()




message = input()
# num = num (from the function num)
num = input_num("hello", 234)

print(num)
print(type(num))




# some_list = [1, 2, 3]

# for i in some_list: 
#     print(i)


foo = 12
bar = foo 

bar = 43


grid = [[' '*3]*3]

foo = [1, 2, 3]
bar = foo.copy()

bar[0] = 321

# foo[0]


