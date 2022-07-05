
class CuentaBancaria:
    nombre_banco = "Banco de Talca"
    accounts = []

    def __init__(self, tasa_interes,balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.accounts.append(self)


    def deposit(self, amount): # se crea la funcion que hace el deposito
        self.balance += amount
        return self

    def withdraw(self,amount): # se crea la funcion que hace el giro
        if(self.balance - amount) >= 0:
            self.balance -= amount
        
        else:
            print("monto insuficiente: cobro de una tasa de $5 pesos")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"balance: {self.balance}")
        return self

    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)
        return self

    @classmethod
    def print_todas_las_cuentas(cls):
        for account in cls.accounts:
            account.display_account_info()


ahorros = CuentaBancaria(.05,1000)
cuenta_corriente = CuentaBancaria(.02,5000)

ahorros.deposit(10).deposit(20).deposit(40).withdraw(600).generar_interes().display_account_info()
cuenta_corriente.deposit(100).deposit(200).deposit(400).withdraw(60).generar_interes().display_account_info()

CuentaBancaria.print_todas_las_cuentas()





