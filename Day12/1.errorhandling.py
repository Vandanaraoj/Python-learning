# a=10/0   # ZeroDivisionError: division by zero
# print(a)

try :
    b=int(input("Enter a number: "))  # ValueError: invalid literal for int() with base 10
    c=int(input("Enter another number: "))  # ValueError: invalid literal for int() with base 10
    result=b/c   # ZeroDivisionError: division by zero
    print(result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("you cannot divide by zero")
else:
    print("Division is successful")
finally:
    print("This block will always execute")    