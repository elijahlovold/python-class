from base_player import BasePlayer
from weapon import Weapon


class Player(BasePlayer): 
    num_players = 0

    def __init__(self, init_name: str, init_race: str="human") -> None: 
        super().__init__(init_name, init_race)

        Player.num_players += 1

        self.p_class = "bard"

    def give_weapon(self, some_weapon: Weapon): 
        print("yay you got a weapon!")
        self.weapon = some_weapon

    def attack_player(self, other_player: "Player"): 
        if (self.level > other_player.level): 
            if (isinstance(self.weapon, Weapon)): 
                self.weapon.kill_message()
            else: 
                print("you died to someone with no weapons, yikes.")

