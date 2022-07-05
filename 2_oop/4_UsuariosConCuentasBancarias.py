class BankAccount:
    nombre_banco = "Banco de Talca"
    accounts = []
    def __init__(self,int_rate,balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self,amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Monto insuficiente: cobro de una tasa de $5 pesos")
            self.balance -= 5
        return self
    
    def display_account_info(self):
        return f"{self.balance}"

    def yeild_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()


class User:

    def __init__(self, name):
        self.name = name
        self.account = {
            "checking" : BankAccount(.02,1000), # MONTO DE CUENTA CORRIENTE $ 1000 DOLARES GENERA UN INTERES DE 2%
            "savings" : BankAccount(.05,3000) # MONTO EN CUENTA DE AHORRO $ 3000 DOLARES GENERA UN INTERES  DE 5%
        }
        

    def display_user_balance(self):
        print(f"User: {self.name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.name}, Savings Balance: {self.account['savings'].display_account_info()}")
        return self

    def transfer_money(self,amount,user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self


Andres = User("Andres Becerra")

Andres.account['checking'].deposit(100).withdraw(100) # LUEGO ACA ANDRES BECERRA HIZO UN DEPOSITO Y UN RETIRO A LA CUENTA CORRIENTE
Andres.display_user_balance()

# BALANCE CUENTA CORRIENTE $ 10OO
# BALANCE CUENTA DE AHORRO $ 3000