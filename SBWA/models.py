class User():
    def __init__(self, name):
        self.name = name

    def show_details(self):
        x = "Personal details"
        y = "name; " + self.name
        z = "Account balance is now #" + str(self.balance)
        result = [x,y,z]
        return result


#child class
class Bank(User):
    def __init__(self, name):
        super().__init__(name)
        self.balance = 500

    def deposit(self, amount):
        self.amount = int(amount)
        self.balance = self.balance + self.amount

        return "Account balance is now #" + str(self.balance)

    def withdraw(self, amount):
        self.amount = int(amount)
        if self.amount > self.balance:
            return "Insufficient funds #" + str(self.balance)
        else:
            self.balance = self.balance-self.amount
            return "Account balance is  now #" + str(self.amount)


    def view_balance(self):
        return self.show_details()
