# file = open("test.txt", "r")

# # Open the CSV file
# with open("test.txt", "r") as file:
#     user_str = file.read()

user_str = input("input some string: ")

list_of_vowels = "aeiou"
list_of_vowels_w_y = "aeiouy"
# list_of_vowels = ["a", "e", "i", "o", "u"]


num_vowels = 0
num_vowels_w_y = 0
for char in user_str: 
    if char in list_of_vowels: 
        num_vowels += 1

    if char in list_of_vowels_w_y: 
        num_vowels_w_y += 1

print("num of vowels: ", num_vowels)
print("num of vowels with y: ", num_vowels_w_y)
