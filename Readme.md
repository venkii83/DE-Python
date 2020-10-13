#Basic Banking Mgmt System:
#About The Project
#The project has been divided in to three sections:
1 - Customers
2 - Bank Account
3 - Employees
#The project tries to depict a basic framework for a retail bank with customers,employees & bank accounts.

#Built With - Python 3.7
#Getting Started
#The initial system will show up customer details such as name, age , gender leading to
#the kind of accounts(checking/savings) he/she holds with the bank:
#Usage
#The bank account shows up basic functions such as deposit, withdrawal & view balance
#The deposit function is created to add a new amount to the existing balance everytime a deposit is made
#The withdraw function is defined to allow withdrawals only if the withdrawal amount is lesser than the balance
#The View balance function is self-explanatory 
# Subclasses under the Bank Account class:
Checking account
Savings account
#Checking account - A deposit follows the same rule as above however the withdrawal
# process incurs a fee if the amount is greater than the daily limit.
#Savings account - A deposit here entails interest based on the simple interest formula
#Exception -BankAccount - If the account balance is below zero then an error message
#will show up everytime the account is viewed unless the balance is readjusted

#The third class is for employees:
#The employees show up basic information such as name & salary;
# It also defines the minimum salary and max raise to be given to the employee
#A salary error will show up if the salary of the employee is less than the defined minimum salary
#Sub class - Employee- Manager:
#The Manager class follows similar parameters like the employee class however
#in the raise section the manager is also entailed to a bonus
#Apart from the Salary error as mentioned above there is also a bonus error criteria
#for the Manager class.