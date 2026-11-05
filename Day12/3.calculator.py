try:
    a=int(input("Enter a number"))
    b=int(input("Enter another number"))
    operator=input("Enter the operation (+, -, *, /)")
    if operator=="+":
        result=a+b
    elif operator=="-":
        result=a-b
    elif operator=="*":
        result=a*b
    elif operator=="/":
        result=a/b
    print("Result", result)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("You cannot divide by zero")
except NameError:
    print("Please enter a valid operator")    
else:
    print("Calculation is successful")
finally:
    print("Program is completed")