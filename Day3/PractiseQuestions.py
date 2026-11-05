# # 1. Scholarship eligibility
attendance = int(input("Enter attendance percentage: "))
marks = int(input("Enter marks: "))
if attendance >= 75:
    if marks >= 90:
        print("Eligible for scholarship")
    else:
        print("Not eligible for scholarship, marks is less than 90")
else:
    print("Not eligible for scholarship, attendance is less than 75%") 

# # # 2. Customer withdrawal eligibility
balance = float(input("Enter account balance: "))
withdraw = float(input("Enter withdrawal amount: "))
daily_limit = float(input("Enter daily limit: "))

if withdraw <= balance and withdraw <= daily_limit:
    print("Withdrawal Successful")
elif withdraw > balance and withdraw <= daily_limit:
    print("Withdrawal Failed: Insufficient Balance")
elif withdraw <= balance and withdraw > daily_limit:
    print("Withdrawal Failed: Exceeds Daily Limit")
else:
    print("Withdrawal Failed: Insufficient Balance and Exceeds Daily Limit")

# 3. Login with username and password    

correct_username = "Vandana"
correct_password = "Rao@123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == correct_username and password == correct_password:
    print("Login Successful")
elif username != correct_username and password == correct_password:
    print("Invalid Username")
elif username == correct_username and password != correct_password:
    print("Invalid Password")
else:
    print("Invalid Username and Password")

# 4. Signal
Signal = input("Enter the signal colour: ").lower()
match Signal:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Get Ready")
    case _:
        print("Invalid signal colour")


#Days of the week
from re import match


day = int(input("Enter day of the week"))
if day==1 :
    print("Monday")
elif day==2:
    print("Tuesday")
elif day==3:
    print("Wednesday")
elif day==4:
    print("Thursday")
elif day==5:
    print("Friday")
elif day==6:
    print("Saturday")
elif day==7:
    print("Sunday")
else:
    print("Invalid day")

# using match case
day = int(input("Enter day of the week"))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")