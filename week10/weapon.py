from base_item import BaseItem

class Weapon(BaseItem): 
    def __init__(self, name): 
        super().__init__(name)

        self.damage = 10
        self.attack_type = "ranged"
    
