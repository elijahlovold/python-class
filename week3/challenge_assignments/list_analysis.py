list_of_items = []

print("input list elements! When finished, type \\n")

# now, loop and add elements to the list
user_input = ""
while True:
    user_input = input("input an element: ")
    if user_input == "\\n": 
        break

    # if we didn't break, i.e., it is a valid input, append to our list
    list_of_items.append(user_input)


# now, print some analytics: 
print(f"your list: {list_of_items}")

print(f"your list has {len(list_of_items)} elements")


# see if the list is only all numbers
only_number = True
for item in list_of_items: 
    try: # try converting to number
        int(item)
    except:
        only_number = False

# if all elements are numbers, computer some analytics
if only_number: 
    num_el = len(list_of_items)
    list_of_ints = [0]*num_el
    for i in range(num_el): 
        list_of_ints[i] = int(list_of_items[i])

    sum = 0
    for item in list_of_ints: 
        sum += item

    print(f"sum of items = {sum}")

    average = sum/num_el
    print(f"average of items = {average}")

    max = list_of_ints[0]
    min = list_of_ints[0]
    for item in list_of_ints:
        if item > max: 
            max = item
        if item < min: 
            min = item

    print(f"max item = {max}")
    print(f"min item = {min}")


# if an element it not a number, computer some analytics about the str
if not only_number: 
    number_of_words = 0
    number_of_chars = 0

    # loop through the list to count words and chars
    for item in list_of_items: 
        is_space = False

        # now loop through the entry to see if multiple words were entered
        first_word_found = False
        for char in item: 
            # only check if a word has been found
            if first_word_found: 
                if char == " ": 
                    is_space = True

                if is_space and char != " ": 
                    number_of_words += 1
                    is_space = False

            if char != " ": 
                first_word_found = True

            number_of_chars += 1

        number_of_words += 1

    print(f"number of words: {number_of_words}")
    print(f"number of chars: {number_of_chars}")


