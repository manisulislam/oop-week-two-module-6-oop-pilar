

class Device:
    def __init__(self, brand, price, color):
        self.brand=brand
        self.price=price
        self.color=color
    def run(self):
        print(f"running laptop : {self.brand}")

class Laptop:
    def __init__(self,memory):
       
        self.memory=memory
    
    def coding(self):
        return f"Learning python and practicing"

class Phone:
    def __init__(self,dual_sim):
        
        self.dual_sim= dual_sim
    
    
    def phone_call(self, number,sms):
        return f"phone number : {number} with {sms}"
    def __repr__(self) -> str:
        return f"phone : {self.dual_sim}"

class Camera:
    def __init__(self, pixel):
       
        self.pixel= pixel
   
    def change_lens(self):
        pass

my_phone= Phone(True)
print(my_phone)