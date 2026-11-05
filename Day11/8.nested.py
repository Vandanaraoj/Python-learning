def calculatetotal(price,tax):
    def calculate_tax():
        return price*tax/100
    return price+calculate_tax()
print(calculatetotal(1000,10))