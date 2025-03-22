from player import Player
from npc import Npc
from tool import Tool
from weapon import Weapon

# foo = int("234")

# joe = Player("joe", "dragon")
# joe.level = 324
# joe.give_weapon(Weapon("bow"))

# brett = Player("brett", "dragon")

# joe.attack_player(brett)

glar = Npc("glar")

bow = Weapon("bow")
bow.attack_type = "ranged"

glar.give_weapon(bow)

print(glar)
