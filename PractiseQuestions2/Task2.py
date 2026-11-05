# Question 1
password="vandana123"
user_pwd=input("Enter your password: ")
print(password==user_pwd)

# Question 2
email1=input("Enter your email1: ")
email2=input("Re-enter your email2: ")
print(email1==email2)\

# Question 3
balance=int(input("Enter your balance: "))
print(f"balance sufficient? {balance>=1000}")

# Question 4
seatsbooked=int(input("Enter the number of seats booked: "))
available_seats=int(input("Enter the number of available seats: "))
print(f"Is available seats greater than booked seats {seatsbooked < available_seats}")

# Question 5
amount=int(input("Enter the amount: "))
print(f"Is amount greater than 2000 {amount > 2000}")

# Question 6
student1=int(input("student absent: "))
print(f"Is student absent greater than 10 days {student1 > 10}")

# Question 7
order_amount=int(input("Enter the order amount: "))
print(f"Is order amount greater than 900 {order_amount > 900}")

# Question 8
cart_value = int(input("Enter the cart value: "))

if cart_value >= 1500:
    discount = cart_value * 20 / 100
    final_amount = cart_value - discount
    print("Eligible for 20% discount")
    print("Discount:", discount)
    print("Final Amount:", final_amount)

elif cart_value == 1499:
    print("1 has been added to your cart.")
    cart_value += 1
    discount = cart_value * 20 / 100
    final_amount = cart_value - discount
    print("Cart Value:", cart_value)
    print("Eligible for 20% discount")
    print("Discount:", discount)
    print("Final Amount:", final_amount)

elif cart_value == 1498:
    print("You are just 2 away from the discount!")
    print("Buy any item below 10 to become eligible.")
    print("Suggestions:")
    print("Candy - 2")
    print("Chocolate - 5")
    print("Pencil - 7")
    print("Eraser - 8")

else:
    amount_needed = 1500 - cart_value
    print("Not eligible for discount.")
    print("Add items worth", amount_needed, "more to get 20% discount.")