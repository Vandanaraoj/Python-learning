try:
    # Get today's sales amount
    sales = int(input("Enter today's sales amount: "))

    # Append the new sales entry
    with open("sales_log.txt", "a") as f:
        f.write(str(sales) + "\n")

    # Read the updated file
    with open("sales_log.txt", "r") as f:
        lines = f.readlines()

        print("Total entries:", len(lines))
        print("Latest entry:", lines[-1].strip())

except FileNotFoundError:
    print("Error: sales_log.txt not found")