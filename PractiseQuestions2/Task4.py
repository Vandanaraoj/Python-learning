# Question 1
main_switch=int(input("Enter main switch status: "))
emergency_switch=int(input("Enter emergency switch status: "))
print(f"will machine run: {main_switch & emergency_switch}")

# Question 2
email = 1
mobile = 0
print(email | mobile)

# Question 3
judge1 = 1
judge2 = 0
print(judge1 ^ judge2)

# Question 4
signal = 5
print(~signal)

# Question 5
memory = 15
print(memory << 1)

# Question 6
population = 800
print(population >> 1)

# Question 7
permission = 4
# Add permission
permission = permission | 2
# Check permission
print(permission & 2)
# Remove permission
permission = permission & (~2)
print(permission)