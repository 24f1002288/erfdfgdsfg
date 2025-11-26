[1,4,"hello",{1:4}]

# Bank : 
# Users : {Corporate, Normal} , Account : {Savings, Current},
# Employees: {Mangaers, Normal}

user_list = [
    {"name":"Kartik","balance":1000},
    {"name":"Amul.inc","balance":1000000, "GSTIN":1909 }
]



a = list({1,2,3})
print(a)

class NormalUser:
    # class variable : shared by all objects of the class
    TOTAL_USERS = 0

    # Constructors
    # Runs automatically when we create a new object
    # used to set initaial "state" of the object
    def __init__(self,_name):
        # instance variables
        self.name = _name
        self.balace = 0 # default attribute
        NormalUser.TOTAL_USERS += 1

    def notification(self):
        return f"Hi {self.name}! , your balance is {self.balace}."
    def add_balance(self, amount:float):
        self.balace += amount
    def transfer(self,amount,user):
        self.balace -= amount
        user.balace += amount 
    def withdraw(self,amount):
        self.balace -= amount


# user_count = how many normal users are there

u1 = NormalUser("Kartik")
print(u1.name)

print(u1.notification()) 
u1.add_balance(40)
print(u1.notification())

u2 = NormalUser("Jagrit")
print(u2.notification())

u1.transfer(100,u2)

print(NormalUser.TOTAL_USERS)
print(u1.TOTAL_USERS)
print(u2.TOTAL_USERS)







# class Car:
#     def __init__(self,_model,_year,_color,_speed):
#         self.model = _model
#         self.year = _year
#         self.color = _color
#         self.speed = _speed




