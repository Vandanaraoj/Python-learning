# Task 1: Library Inventory Reader

try:
    # Part A: Read line by line
    with open("books.txt", "r") as f:
        count = 0

        for line in f:
            title, author, year = line.strip().split(",")
            if int(year) > 2015:
                count += 1

        print("Books after 2015:", count)

    # Part B: Read the entire file
    with open("books.txt", "r") as f:
        data = f.read()

        years = []

        for line in data.strip().split("\n"):
            title, author, year = line.split(",")
            years.append(int(year))

        print("Oldest book year:", min(years))

except FileNotFoundError:
    print("Error: books.txt not found")