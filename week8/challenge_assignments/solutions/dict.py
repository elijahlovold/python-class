# Write a function that checks if a key exists in a nested dictionary.
def key_in_nested_dict(d: dict, key: str) -> bool:
    """Recursively check if a key exists in a nested dictionary."""
    pass

def create_character(
        name: str, 
        char_class: str, 
        race: str, 
        strength: int, 
        agility: int, 
        intelligence: int
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
    - level: int, overall character level

    Returns:
    - dict: character stats including name, class, race, level, and attributes
    """
    pass

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
    pass

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
        "Level: 1"

    Parameters:
    - character: dict, the character whose stats to display
    """
    pass
