from weapon import Weapon
from tool import Tool

class BasePlayer(): 
    def __init__(self, init_name: str, init_race: str="human") -> None: 
        self.name = init_name
        self.race = init_race

        self.strength = 10
        self.agility = 123
        self.intelligence = 1
        self.level = 0

        self.weapon: None | Weapon = None
        self.tool: None | Tool = None 

    
    def give_weapon(self, some_weapon: Weapon): 
        print("yay you got a weapon!")
        self.weapon = some_weapon

    def give_tool(self, some_tool: Tool): 
        print("yay you got a tool!")
        self.tool = some_tool

    def __str__(self) -> str: 
        stats = ""
        stats += "Name:" + self.name
        stats += "\nRace:" + self.race
        stats += "\nLevel:" + str(self.level)
        stats += "\nStrength:" + str(self.strength)
        stats += "\nAgility:" + str(self.agility)
        stats += "\nIntelligence:" + str(self.intelligence)

        if (isinstance(self.tool, Tool)): 
            stats += "\nTool: " + str(self.tool)
        if (isinstance(self.weapon, Weapon)): 
            stats += "\nWeapon: " + str(self.weapon)

        return stats + "\n"

