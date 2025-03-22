
from base_player import BasePlayer

class Npc(BasePlayer): 
    num_npcs = 0

    def __init__(self, init_name: str, init_race: str="human") -> None: 
        super().__init__(init_name, init_race)

        Npc.num_npcs += 1

