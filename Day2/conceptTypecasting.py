Name = input("Enter your name: ")
Age = int(input("Enter your age: "))
Age = Age + 1

# print("Hello " + Name + ", your age is " + str(Age))  >> Concatination of string and integer is not possible, so we need to convert the integer to string using str() function.
# print("Hello", Name, ", your age is", Age)

print(f"Hello {Name}, Your age is {Age}")