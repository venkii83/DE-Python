class Customers:

    def __init__(self, firstname, lastname, age, gender):
        """Create __init__() method with name, age & gender of the customer"""
        self.name = name = ""
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Customer details")
        print("")
        print("name", self.name)
        print("age", self.age)
        print("gender", self.gender)

class BankAccount:
    def __init__(self:
        self.balance = 0

    def deposit(self, amount):
        """Defining the deposit amount and it's calculation"""
        self.amount = amount
        self.balance = self.balance + self.amount
        print("Account balance updated", self.balance)

    def withdraw(self, amount):
        """Defining the withdrawal procedure"""
        self.amount = amount
        if self.amount > self.balance:
            print("Insufficient balance", self.balance)
        else:
            self.balance = self.balance - self.amount
            print("Account bal has been updated: $", self.balance)

    def View_balance(self):
        """Defining the view balance options"""
        self.show_details()
            print("Account bal has been updated: $", self.balance)


class CheckingAccount(BankAccount):
        """Defining checking account & its characterstics"""
    def __init__(self, balance, limit):
        """Calling the parent constructor using Class name __init__"""
        BankAccount __init__(self, balance)
        self.limit = limit
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount, fee):
        if fee <= self.limit:
            BankAccount.withdraw(self, amount - fee)
        else:
            BankAccount.withdraw(self, amount - self.limit)


class SavingsAccount(BankAccount):
        """Defining savings account & its characterstics"""
    def __init__(self, balance, interest_rate):
        """Calling the parent constructor using Class name __init__"""
        BankAccount __init__(self, balance)
        self.interest_rate = interest_rate
        """New Functionality"""
    def compute_interest(self, n_years =1):
        return self.balance * ((1 + self.interest_rate) ** n_years - 1)


class BalanceError(Exception): pass
        """Defining exceptions/errors"""
class BankAccount:
    def __init__(self, name, balance):
        if balance < 0:
            raise BalanceError("Balance has to be non-negative")
        else:
            self.name, self.balance = name, balance

class Employee:
    def __init__(self, name, salary=50000):
        self.name = name
        self.salary = salary

    def give_raise(self, amount):
    """Add a give_raise method"""
        self.salary += amount

    """Defining a sub class Manager"""
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=80000, project=None)
        Employee.__init__(self, name, salary)
        self.project = project

    """Add a give_raise method"""
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)



class SalaryError(ValueError):
    """Define SalaryError inherited from ValueError"""
    pass
class BonusError(SalaryError):
    """Define BonusError inherited from SalaryError"""
    pass

class Employee:
    MIN_SALARY = 50000
    MAX_RAISE = 5000

    def __init__(self, name, salary=50000):
        self.name = name
        self.salary = salary

    """If salary is too low"""
        if salary < MIN_SALARY:
            # Raise a SalaryError exception
            raise SalaryError("Salary is too low!")

        self.salary = salary
