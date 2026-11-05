# #Convert minutes into hr and remaining minutes 
# a=150
# b= a//60
# c= a%60
# print("Hours:", b, "Minutes:", c)

# #Discount calculation
# original_price = 5000
# discount_percentage = 60
# discount_amount = (discount_percentage / 100) * original_price
# final_price = original_price - discount_amount
# print("Final Price:", final_price)

#Sqrt of number 

# num = int(input("Enter a number: "))
# i = 0
# while i * i <= num:
#     i += 1
# print("Integer square root =", i - 1)


# #no.of.weeks  and days in a given number of days
# days =47
# weeks = days // 7
# remaining_days = days % 7
# print("Weeks:", weeks, "Days:", remaining_days)


#  Find the largest number
# x=int(input("Enter first number: "))
# y=int(input("Enter second number: "))
# if x>y:
#     print(f"{x} is the largest number.")
# else:
#     print(f"{y} is the largest number.")

# # If  elseif statement
# Signal = input("Enter the signal colour: ").lower()
# if Signal == "red":
#     print("Stop")   
# elif Signal == "green":
#         print("Go")
# elif Signal == "yellow":
#         print("Get Ready")
# else:
#     print("Invalid signal colour")

#Scholarship eligibility
# attendance = int(input("Enter attendance percentage: "))
# marks = int(input("Enter marks: "))
# if attendance >= 75:
#     if marks >= 90:
#         print("Eligible for scholarship")
#     else:
#         print("Not eligible for scholarship, marks is less than 90")
# else:
#     print("Not eligible for scholarship, attendance is less than 75%")        

# Calulator menu
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation +, -, *, /: ")
match operation:
    case "+":
              print(num1 + num2)
    case "-":
                print(num1 - num2)
    case "*":
                print(num1 * num2)
    case "/":
                print(num1 // num2)
    case _:
                print("Invalid operation")            