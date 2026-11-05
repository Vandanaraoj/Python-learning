# Question 1
amount=int(input("Enter the amount: "))
city=input("Enter the city: ")
print(f"eligible for free delivery: {amount > 2000 and city == 'Bangalore'}")

# Question 2
seat_available=True
payment=True
print(f"Able to book movie ticket: {seat_available and payment}")

# Question 3
premium_customer=True
purchase=15
print(f" Eligible for festive gift: {premium_customer or purchase > 20}")

# Question 4
stock_available=True
print(f"place order: {stock_available}")

# Question 5
Damaged=False
print(f"Dispatched ?: {Damaged}")

# Question 6
username_correct = True
password_correct = True
account_blocked = False
print(f"Login successful: {username_correct and password_correct and not account_blocked}")

# Question 7
seat_available = False
vip_pass = True
print(seat_available or vip_pass)