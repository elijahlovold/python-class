def count_vowels(user_str: str, count_y = False) -> int: 
    vowels = "aeiouAEIOU"
    if count_y: 
        vowels += "yY"

    num_vowels = 0
    for char in user_str: 
        if char in vowels: 
            num_vowels += 1

    return num_vowels

user_str = input("input some string: ")

print("vowels without y:    ", count_vowels(user_str))
print("vowels with y:       ", count_vowels(user_str, True))

