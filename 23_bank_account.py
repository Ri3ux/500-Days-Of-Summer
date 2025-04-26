"""
Definimos una clase BankAccount que representa una cuenta bancaria
La clase tiene un constructor que inicializa el titular de la cuenta y el saldo.
También tiene métodos para depositar, retirar, activar y desactivar la cuenta.
"""

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True

    def deposit(self, amount):
        if self.is_active:
            self.balance += amount
            print(f"{self.account_holder}, has depositado ${amount}. Tu saldo actual es ${self.balance}")
        else:
            print(f"{self.account_holder}, no puede realizarse la transacción. Tu cuenta está inactiva.")
    
    def withdraw(self, amount):
        if self.is_active:
            if amount <= self.balance:
                self.balance -= amount
                print(f"{self.account_holder}, has retirado ${amount}. Tu saldo actual es ${self.balance}")
            else:
                print(f"{self.account_holder}, no tienes fondos suficientes para realizar la transacción.")
        else:
            print(f"{self.account_holder}, no podemos realizar la transacción. Tu cuenta está inactiva.")
    
    def deactivate(self):
        self.is_active = False
        print(f"Hemos desactivado la cuenta de {self.account_holder}.")
    
    def activate(self):
        self.is_active = True
        print(f"Hemos activado la cuenta de {self.account_holder}.")

# Creamos dos instancias de la clase BankAccount
account_1 = BankAccount("Juan", 1000)
account_2 = BankAccount("Ana", 2000)

# Realizamos algunas operaciones con las cuentas llamando a los métodos de la clase BankAccount
account_1.deposit(500)
account_2.withdraw(300)
account_1.deactivate()
account_1.withdraw(100) # No se puede retirar porque la cuenta está inactiva
account_2.withdraw(2500) # No se puede retirar porque no hay fondos suficientes