def clean_input(data):

    customer, amount = data

    customer = customer.strip()

    print("\nCleaned Customer:", customer)
    print("Cleaned Amount:", amount)

    return customer, amount


def apply_discount(data):

    customer, amount = data

    discount = amount * 0.10

    final_amount = amount - discount

    print("Discount:", discount)
    print("Amount After Discount:", final_amount)

    return customer, final_amount


def format_currency(data):

    customer, amount = data

    formatted_amount = f"₹{amount:.2f}"

    print("Formatted Amount:", formatted_amount)

    return customer, formatted_amount


def process_invoice(data):

    print("\n--- Task 9: Functional Pipeline ---")

    step1 = clean_input(data)

    step2 = apply_discount(step1)

    step3 = format_currency(step2)

    return step3


invoice = ("  Vandana  ", 5000)

final_invoice = process_invoice(invoice)

print("Final Invoice:", final_invoice)