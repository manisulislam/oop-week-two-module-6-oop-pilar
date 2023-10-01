class Vehicle:
    def __init__(self,name , price) -> None:
        self.name= name
        self.price= price
    def move(self):
        return f"move"
    def __repr__(self) -> str:
        return f"{self.name} {self.price}"

class Bus(Vehicle):
    def __init__(self, name, price,seat) -> None:
        self.seat=seat
        super().__init__(name, price)
    def __repr__(self) -> str:
        return super().__repr__()
class Track(Vehicle):
    def __init__(self, name, price, weight) -> None:
        self.weight= weight
        super().__init__(name, price)

class Pickup(Track):
    def __init__(self, name, price, weight) -> None:
        super().__init__(name, price, weight)


class ACBus(Bus):
    def __init__(self, name, price, seat, temperature) -> None:
        self.temperature= temperature
        super().__init__(name, price, seat)
    def __repr__(self) -> str:
        print(self.seat)
        return super().__repr__()

greenline= ACBus("greenline", 12502, 20,27)

print(greenline.name)
print(greenline.price)