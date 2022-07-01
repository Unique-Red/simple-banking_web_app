import random

class User():
    
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def show_details(self):
        x = "Personal details"
        y = "name: " + self.name
        z = "Account balance is now #" + str(self.balance)
        a = "Account number is " + str(self.number)
        result = [x,y,a,z]
        return result


#child class
class Bank(User):
    def __init__(self, name, number):
        super().__init__(name, number)
        self.balance = 0

    def initial_deposit(self, initial):
        self.initial = int(initial)
        if self.initial < 500:
            return "Initial deposit shold be minimum of #500"
        else:
            self.balance = self.balance + self.initial
            return "Initial deposit is #" + str(self.balance)

    def deposit(self, amount):
        self.amount = int(amount)
        if self.amount > 1000000:
            return "You cannot deposit more than one million naira at a time"
        elif 100 > self.amount:
            return "You cannot deposit less than 100 naira at a time"

        elif (self.balance + self.amount) > 1000000:
            return "Account cannot take more one million naira"
            
        else:
            self.balance = self.balance + self.amount
            return "Account balance is now #" + str(self.balance)

    def withdraw(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return "Insufficient funds. Your currently have #" + str(self.balance)
        else:
            self.balance = self.balance-self.amount
            return "Account balance is  now #" + str(self.amount)


    def view_balance(self):
        return self.show_details()

# red = Bank("redx", random.randint(1000000000, 9999999999))
# red = Bank("redx", 3783008667)
# print(red.show_details())
# # print(red.initial_deposit(500))
# # print(red.show_details())
# print(red.deposit(1000))
# print(red.show_details())
# print(red.deposit(99999))
# print(red.show_details())
# # print(red.withdraw(10000))