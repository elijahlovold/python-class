# dictionaries

# say you have a list like this
character = ["jeff", 21, 5.8, 168, [["ham", "turkey"], ["apple", "banana"]]]

print(character)

# if you want the name
name = character[0]
print(name)


# can remake using keys to set the attributes
character = {
        "name": "jeff", 
        "age": 21, 
        "height": 5.8, 
        "foods": {
            "proteins": ["ham", "turkey"],
            "fruit": ["apple", "banana"]
            },
    }

# easier to access like this
foods = character["foods"]
list_of_proteins = foods["proteins"]

print(foods)
print(list_of_proteins)
