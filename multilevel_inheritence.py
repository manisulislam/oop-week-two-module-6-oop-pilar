

class Device:
    def __init__(self, brand, price, color, origin):
        self.brand=brand
        self.price=price
        self.color=color
        self.origin = origin
    def run(self):
        print(f"running laptop : {self.brand}")

class Laptop:
    def __init__(self,memory):
       
        self.memory=memory
    
    def coding(self):
        return f"Learning python and practicing"

class Phone(Device):
    def __init__(self,brand,price, color, origin,dual_sim):
        self.dual_sim= dual_sim
        super().__init__(brand,price, color, origin)
    
    def phone_call(self, number,sms):
        return f"phone number : {number} with {sms}"
    def __repr__(self) -> str:
        return f"phone : {self.brand} {self.price} {self.dual_sim}"

class Camera:
    def __init__(self, pixel):
       
        self.pixel= pixel
   
    def change_lens(self):
        pass

my_phone= Phone("samsung",21000,"gold","bangladesh",True)
print(my_phone.brand)
print(my_phone)