# [1,4,"hello",{1:4}]

# Bank : 
# Users : {Corporate, Normal} , Account : {Savings, Current},
# Employees: {Mangaers, Normal}

# user_list = [
#     {"name":"Kartik","balance":1000},
#     {"name":"Amul.inc","balance":1000000, "GSTIN":1909 }
# ]



# a = list({1,2,3})
# print(a)

# class NormalUser:
#     # class variable : shared by all objects of the class
#     TOTAL_USERS = 0

#     # Constructors
#     # Runs automatically when we create a new object
#     # used to set initaial "state" of the object
#     def __init__(self,_name):
#         # instance variables
#         self.name = _name
#         self.balace = 0 # default attribute
#         NormalUser.TOTAL_USERS += 1

#     def notification(self):
#         return f"Hi {self.name}! , your balance is {self.balace}."
#     def add_balance(self, amount:float):
#         self.balace += amount
#     def transfer(self,amount,user):
#         self.balace -= amount
#         user.balace += amount 
#     def withdraw(self,amount):
#         self.balace -= amount


# # user_count = how many normal users are there

# u1 = NormalUser("Kartik")
# print(u1.name)

# print(u1.notification()) 
# u1.add_balance(40)
# print(u1.notification())

# u2 = NormalUser("Jagrit")
# print(u2.notification())

# u1.transfer(100,u2)

# print(NormalUser.TOTAL_USERS)
# print(u1.TOTAL_USERS)
# print(u2.TOTAL_USERS)


# class savingAccount:
#     COUNT_ACCOUNTS = 0
    
#     def __init__(self,user,pan_no):
#         self.user = user
#         self.pan_no = pan_no
#         self.balance = 0
#         self.int_rate = 0.05
#         self.acc_no = savingAccount.COUNT_ACCOUNTS

#         savingAccount.COUNT_ACCOUNTS += 1
    
#     def __repr__(self):
#         return f"Account: {self.acc_no} belonging to {self.user}! , with balance {self.balance}."

#     def notification(self):
#         return f"Hi {self.user}! , your balance is {self.balace}."
#     def add_balance(self, amount:float):
#         self.balace += amount
#     def transfer(self,amount,account):
#         self.balace -= amount
#         account.balace += amount 
#     def withdraw(self,amount):
#         self.balace -= amount
#     def interest(self):
#         self.balace += self.balace * self.int_rate

# class currentAccount:
#     COUNT_ACCOUNTS = 0
#     CHARGE = 500
    
#     def __init__(self,user,gst_no):
#         self.user = user
#         self.gst_no = gst_no
#         self.balance = 0
#         self.acc_no = currentAccount.COUNT_ACCOUNTS

#         currentAccount.COUNT_ACCOUNTS += 1
    
#     def __repr__(self):
#         return f"Account: {self.acc_no} belonging to {self.user}! , with balance {self.balance}."
    
#     def notification(self):
#         return f"Hi {self.user}! , your balance is {self.balace}."
#     def add_balance(self, amount:float):
#         self.balace += amount
#     def transfer(self,amount,account):
#         self.balace -= amount
#         account.balace += amount 
#     def withdraw(self,amount):
#         self.balace -= amount
#     def charge(self):
#         self.balace -= currentAccount.CHARGE


# u1 = savingAccount("Hardik",123)
# print(u1)
# u2 = currentAccount("Tata","456")
# print(u2)
    

class account:
    COUNT_ACCOUNTS = 0
    
    def __init__(self,user):
        self.user = user
        self.balance = 0
        self.acc_no = savingAccount.COUNT_ACCOUNTS

        account.COUNT_ACCOUNTS += 1
    
    def __repr__(self):
        return f"Account: {self.acc_no} belonging to {self.user}! , with balance {self.balance}."

    def notification(self):
        return f"Hi {self.user}! , your balance is {self.balace}."
    def add_balance(self, amount:float):
        self.balace += amount
    def transfer(self,amount,account):
        self.balace -= amount
        account.balace += amount 
    def withdraw(self,amount):
        self.balace -= amount



class savingAccount(account):
    INT_RATE = 0.04

    def __init__(self,user,pan_no):
        super().__init__(user)
        self.pan_no = pan_no
    
    def __repr__(self):
        return f"Hello {self.user}! Account: {self.acc_no}, with balance {self.balance}."

    def interest(self):
        self.balace += self.balace * savingAccount.INT_RATE

class currentAccount(account):
    CHARGE = 500

    def __init__(self,user,gst_no):
        super().__init__(user)
        self.gst_no = gst_no
    
    def charge(self):
        self.balace -= currentAccount.CHARGE


u1 = savingAccount("hardik",123)
u2 = currentAccount("Tata",456)
print(u1,u2,sep="\n")





