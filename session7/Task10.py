def dispatch_payment(amount):

    print("\n--- Task 10: Fail-Safe Dispatcher ---")

    if amount <= 0:

        return False, "Payment amount must be greater than zero"

    elif amount > 10000:

        return False, "Payment exceeds transaction limit"

    else:

        return True, None


success, error = dispatch_payment(5000)

print("Success:", success)
print("Error:", error)


success, error = dispatch_payment(0)

print("\nTesting Invalid Payment")
print("Success:", success)
print("Error:", error)


success, error = dispatch_payment(15000)

print("\nTesting Large Payment")
print("Success:", success)
print("Error:", error)