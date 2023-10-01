# ena poribahan
class Company:
    def __init__(self, name, address):
        self.name=name
        self.bus=[]
        self.routes=[]
        self.drivers=[]
        self.counter=[]
        self.manager=[]
        self.supervisor=[]
        self.fare=[]

class Driver:
    def __init__(self, license, name, age):
        self.license=license
        self.name= name
        self.age=age
class Counter:
    def __init__(self):
        pass
    def purchase_a_ticket(self, start, destination):
        self.start=start
        self.destination= destination

class Passenger:
    pass

red_mia= Driver("ad","red_mia", 45)