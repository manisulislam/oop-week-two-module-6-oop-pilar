from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("i need food")
    def move(self):
        pass

class Monkey(Animal):
    def __init__(self,name) -> None:
        self.category= "monkey"
        self.name= name
        super().__init__()
    def eat(self):
        print("monkey eat banana")

dog= Monkey("dogy")
dog.eat()