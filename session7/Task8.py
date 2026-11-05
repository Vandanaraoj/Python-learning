def my_function():

    print("\n--- Task 8: Print vs Return ---")

    print("The result is:", 100)

    # No return statement


result = my_function()

print("Value stored in result:", result)

print("Explanation:")
print("The function prints 100, but it does not return anything.")
print("Therefore, result becomes None.")


# Correct version

def correct_function():

    value = 100

    print("The result is:", value)

    return value


correct_result = correct_function()

print("Stored Correct Result:", correct_result)