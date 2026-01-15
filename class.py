class NewClass:
    def __init__(self):
        self.__private_var = "I am private"

    def __private_method(self):
        return "This is a private method"

    def show_result_private(self):
        return self.__private_var + "and" + self.__private_method()    

newObj = NewClass()
print(newObj.show_result_private())

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number   # Private
        self.__balance = balance                 # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance

account = BankAccount("12345", 1000)

# Direct access will fail
try:
    account.__balance += 500  # ✗ AttributeError
except AttributeError:
    print("Direct access to private variable failed!!!")

# Access using methods
print("Your account balance is: ", account.get_balance())   # ✓ 1000

account.deposit(500)
print("Your account balance after deposit is: ", account.get_balance())  # ✓ 1500