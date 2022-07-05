class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_deposit(self, amount): # se crea la funcion que hace el deposito
        self.amount += amount

    def make_withdrawl(self,amount): # se crea la funcion que hace el giro
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}") # se crea la funcion que hace el balance

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance() # se crea la funcion que hace la transferencia


adrien = User("Adrien")       # usuario
nibbles = User("Mr. Nibbles") # usuario
benny_bob = User("Benny Bob") # usuario

adrien.make_deposit(100) # deposito
adrien.make_deposit(200)
adrien.make_deposit(50)
adrien.make_withdrawl(45) # giro
adrien.display_user_balance()

nibbles.make_deposit(1000)
nibbles.make_deposit(1000)
nibbles.make_withdrawl(500)
nibbles.make_withdrawl(300)
nibbles.display_user_balance()

benny_bob.make_deposit(1500)
benny_bob.make_withdrawl(1000)
benny_bob.make_withdrawl(5000)
benny_bob.make_withdrawl(3000)
benny_bob.display_user_balance()


nibbles.transfer_money(400, adrien) #nibbles trasnfiere 400 a adrien