class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number      # приватний
        self._account_holder = account_holder       # доступний, але “protected”
        self.__balance = balance                    # приватний

    @property
    def account_holder(self):
        return self._account_holder  # тільки читання

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount

    def check_balance(self):
        return self.__balance