class BaseItem(): 
    def __init__(self, name): 
        self.name = name
        self.weight = 0
        self.description = "ranged"

    def kill_message(self): 
        print("you got shot!")

    def __str__(self) -> str: 
        return self.name
