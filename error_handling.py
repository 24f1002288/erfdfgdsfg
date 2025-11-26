# with open("test.txt","r") as file:
#     print(file.read())

# x = 10
# assert x > 15

def alchohol_allowed(user_age:int):
    assert user_age >= 21
    print("alchohol allowed")

# alchohol_allowed("22")

# int("hello")

#"EAFP:Easier to ask for forgiveness than permission"


# handling errors:

# def division(a,b):
#     return a/b
# try:
#     a = int(input("Divident: "))
#     b = int(input("Diviser: "))
#     print(division(a,b))
# except ValueError:
#     print("Invalid Input.")
# except ZeroDivisionError:
#     print("Diviser can not be 0.")
# except:
#      print("Unknown Error.")
# finally:
#     print("Cleaning Memory")

# try:
#     f = open("try.txt",'r')
#     content = f.read()
# except FileNotFoundError:
#     print("No such file exists.")
# except:
#     print("Unknown Error.")
# else:
#     print("File Loading and reading completed.")
# finally:
#     if 'f' in locals():
#         f.close()
#         print("File closed.")
#     print("Cleanup Done.")

# Raising Our own Errors.


def alchohol_allowed(user_age:int):
    if not 0 <= user_age <= 100:
        raise ValueError("Age should be between 0 and 100.")
    if user_age < 21:
        raise IndexError("User is not allowed in our Establishment.")
    print("Welcome")
    
alchohol_allowed(16)
try:
    alchohol_allowed(-1)
except ValueError:
    print("Eneter another input.")
except IndexError:
    print("Get out.")


# 




