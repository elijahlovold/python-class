class BaseItem(): 
    def __init__(self, _weight): 
        self._weight =_weight 

class BaseFood(): 
    def __init__(self, _name: str): 
        self.name = _name

    def eat(self): 
        print("eating: ", self.name)

class Orange(BaseFood): 
    def __init__(self, name: str, color: str="orange"): 
        super().__init__(name)

        self.color = color

    def eat(self): 
        print("eating an orange: ", self.name)

    def peel(self):
        print("peeling...")

class Apple(BaseFood): 
    def cut(self):
        print("cutting...")


foo = Orange("bob")
bar = Apple("Micah")

print(foo.name)
foo.peel()
print(bar.name)
bar.cut()

foo.eat()
bar.eat()
