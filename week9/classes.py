
class Weapon(): 
    def __init__(self, name): 
        self.name_of_weapon = name
        self.damage = 10
        self.attack_type = "ranged"

    def kill_message(self): 
        print("you got shot!")

class Player(): 
    num_players = 0

    def __init__(self, init_name: str, init_race: str="human") -> None: 
        print("hello world, im alive!")
        print("creating playe named: ", init_name)

        Player.num_players += 1

        self.name = init_name
        self.p_class = "bard"
        self.race = init_race

        self.strength = 10
        self.agility = 123
        self.intelligence = 1
        self.level = 0

        self.weapon: None | Weapon = None

        self.print_stats()

    def give_weapon(self, some_weapon: Weapon): 
        if (self.level < 4): 
            return
        print("yay you got a weapon!")
        self.weapon = some_weapon

    def attack_player(self, other_player: "Player"): 
        if (self.level > other_player.level): 
            if (isinstance(self.weapon, Weapon)): 
                self.weapon.kill_message()
            else: 
                print("you died to someone with no weapons, yikes.")

    def __getitem__(self, index): 
        print("halksdjf: ", index)
    
    def __del__(self): 
        print("bye bye")

    def print_stats(self): 
        print("Name:", self.name)
        print("Class:", self.p_class)
        print("Race:", self.race)
        print("Level:", self.level)
        print("Strength:", self.strength)
        print("Agility:", self.agility)
        print("Intelligence:", self.intelligence)
        print("\n")

foo = int("234")

joe = Player("joe", "dragon")
joe.level = 324
joe.give_weapon(Weapon("bow"))

brett = Player("brett", "dragon")

joe.attack_player(brett)

print(type(joe))
