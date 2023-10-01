class Animal:
    def __init__(self, name) -> None:
        self.name= name
    
    def make_sound(self):
        print("making some sound")
    
class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
       print("mew mew")

don= Cat("real don")
don.make_sound()