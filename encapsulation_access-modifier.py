class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name= holder_name #public
        self._branch="sultanpur " #protected
        # self.balance= initial_deposit
        self.__balance= initial_deposit #private
    def deposit(self, amount):
        self.__balance+=amount
    
    def get_balance(self):
        return self.__balance




anis= Bank("anis",50000)
print(anis.holder_name)
# print(anis.balance)
anis.deposit(25000)
anis.holder_name="anisul islam"
print(anis.get_balance())
print(anis._branch)

print(dir(anis))
print(anis._Bank__balance)