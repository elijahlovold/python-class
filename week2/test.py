from random import random

from colorama import Fore, Back

print(Fore.GREEN + "Inventory updated successfully")

some_number = int(random())

# some number between 0 and N
N = 100
some_number = int(random()) % N

# foo = int(input("input some number"))


# some_bool = True
# # some_new_variable = -1
# age = 9234
# if ((age > 56) or (input() == "some value")): 
#     print("is young adult")

#     if (): 
#         pass 

#     elif (): 
#         if (): 
#             pass 

#     else: 
#         pass

# elif ():
#     pass

# # if (age >= 18 and age < 56):  # think of else if
# elif (age < 56):  # think of else if
#     print("is adult")

# foo = 234
# if (foo < 0):  # think of else if
#     print("wow nice")

# else: 
#     if (foo < 56): 
#         print("nvm")

#     elif (foo < 100): 
#         print("nvm")

#     else:
#         print("nvm")

#     if (foo == -1): 
#         print("9234")


# if (foo == -1):  # think of else if
#     print("wow nice")

# elif (foo == 23): 
#     print("nvm")

# elif (foo == 23): 
#     print("nvm")

"""

* input some number 

check the following conditions: 

    number < 56
         print("case 1")

    56 <= number < 100
    100 > number >= 56
         print("case 2")

    number >= 100
         print("case 3")

    -1 == number
    number == -1
        print("case special")
"""

# passwrd = "password" 
# while (True): 
#     guess = input("guess the password: ")
#     if (guess == passwrd): 
#         break
#     else: 
#         print("guess again")

# print("yay you guessed it")

# guess = ""
# while (guess != "quit"): 
#     guess = input("guess the password: ")
#     pass

# some_list = []
# while ((guess := input("guess the password: ")) != "quit"): 
#     some_list ...


# print("yay you guessed it")

# # # list: 
# # create a list of contacts
# str1 = "jarod"
# str2 = "micah"
# str3 = "luke"

list_of_contacts = ["jarod", "micah", "luke"]

# [] = + *

# empty list
some_list = [3, 4, 6, 2, 4, 5]

i = 0
while (i < len(some_list)): 
    some_entry = some_list[i]
    print(some_entry)
    i += 1

some_list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]

for row in some_list: 
    for col in row: 
        print(col)

"""

create an empty list 

while input != 'quit':
    add input onto the list

print list

"""

foo = 234
some_string = "number is " + str(foo) + "!"

some_string = f"number is {foo}!"


