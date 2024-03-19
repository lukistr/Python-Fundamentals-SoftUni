class BankAccount:
    def __init__(self, account_number, balance=0):
        """
        Constructor method to initialize the account number and balance.
        """
        # ✳️ Write code to initialize the account number and balance attributes
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """
        Method to deposit money into the account.
        """
        # ✳️ Write code to add the deposited amount to the balance
        self.balance += amount

    def withdraw(self, amount):
        """
        Method to withdraw money from the account.
        """
        # ✳️ Write code to check if there are sufficient funds and deduct the withdrawn amount from the balance
        self.balance -= amount

    def get_balance(self):
        """
        Method to retrieve the current balance.
        """
        # ✳️ Write code to return the current balance
        return self.balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0):
        """
        Constructor method to initialize the account number, balance, and interest rate.
        """
        # ✳️ Call the superclass constructor to initialize common attributes
        # ✳️ Initialize the interest rate attribute
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate
        BankAccount(self.account_number, self.balance)

    def calculate_interest(self):
        """
        Method to calculate and add interest to the account balance.
        """
        # ✳️ Write code to calculate the interest based on the current balance and interest rate
        # ✳️ Write code to add the calculated interest to the account balance
        self.balance += (self.balance * (self.interest_rate / 100))
        return self.balance


# Testing the functionality of the classes
if __name__ == "__main__":
# ✳️ Create a BankAccount instance with account number "123456789" and initial balance of 1000

# ✳️ Deposit 500 into the account

# ✳️ Withdraw 200 from the account

# ✳️ Get the current balance of the bank account

# ✳️ Create a SavingsAccount instance with account number "987654321", initial balance of 2000, and interest rate of 5%

# ✳️ Deposit 1000 into the savings account

# ✳️ Calculate and add interest to the savings account

# ✳️ Get the current balance of the savings account after adding interest
    account = BankAccount(123456789, 1000)
    account.deposit(500)
    account.withdraw(200)
    print(f'{account.get_balance():.2f}')
    savingAcc = SavingsAccount(123456789, 2000, 10)
    print(f'{savingAcc.calculate_interest():.2f}')
