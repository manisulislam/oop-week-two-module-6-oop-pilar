class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand=brand
        self.price=price
        self.color=color
        self.memory=memory
    def run(self):
        print(f"running laptop : {self.brand}")
    def coding(self):
        return f"Learning python and practicing"

class Phone:
    def __init__(self, brand, price, color, dual_sim):
        self.brand= brand
        self.price= price
        self.color=color
        self.dual_sim= dual_sim
    
    def run(self):
        return f"phone tipa tipi "
    def phone_call(self, number,sms):
        return f"phone number : {number} with {sms}"

class Camera:
    def __init__(self, brand, price, color, pixel):
        self.brand= brand
        self.price= price
        self.color= color
        self.pixel= pixel
    def run(self):
        pass
    def change_lens(self):
        pass