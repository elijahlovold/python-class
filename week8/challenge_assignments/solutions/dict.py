# Write a function that checks if a key exists in a nested dictionary.
def key_in_nested_dict(d: dict, key: str) -> bool:
    """Recursively check if a key exists in a nested dictionary."""
    if key in d.keys(): 
        return True

    for _, item in d.items(): 
        if isinstance(item, dict): 
            if key_in_nested_dict(item, key): 
                return True
    return False

def create_character(
        name: str, 
        char_class: str, 
        race: str, 
        strength: int, 
        agility: int, 
        intelligence: int,
        level: int 
        ) -> dict:
    """
    Creates a character with the given attributes.

    Parameters:
    - name: str, the name of the character
    - char_class: str, the class of the character (e.g., 'warrior', 'mage')
    - race: str, the race of the character (e.g., 'human', 'elf')
    - strength: int, strength attribute of the character
    - agility: int, agility attribute of the character
    - intelligence: int, intelligence attribute of the character

    Returns:
    - dict: character stats including name, class, race, level, and attributes
    """
    return {
            "name": name, 
            "class": char_class, 
            "race": race, 
            "strength": strength, 
            "agility": agility, 
            "intelligence": intelligence, 
            "level": level, 
        }

def level_up(character: dict) -> dict:
    """
    Levels up the character, incrementing the level and boosting attributes.
        level: +1
        strength: +2
        agility: +1
        intelligence: +1

    Parameters:
    - character: dict, the character to level up

    Returns:
    - dict: updated character stats
    """
    character["level"] += 1
    character["strength"] += 2
    character["agility"] += 1
    character["intelligence"] += 1
    return character

def display_stats(character: dict) -> dict:
    """
    Prints the stats of the character.
    
    Format: 
        "Name: Alderan"
        "Class: Warrior"
        "Race: Human"
        "Level: 1"
        "Strength: 10"
        "Agility: 8"
        "Intelligence: 6"

    Parameters:
    - character: dict, the character whose stats to display
    """
    print("Name:", character["name"])
    print("Class:", character["class"])
    print("Race:", character["race"])
    print("Level:", character["level"])
    print("Strength:", character["strength"])
    print("Agility:", character["agility"])
    print("Intelligence:", character["intelligence"])
