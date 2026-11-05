def get_market_rates(ticker):

    print("\n--- Task 4: Currency Arbitrage Scanner ---")

    if ticker == "USD":

        buy_price = 83.50
        sell_price = 84.00

    elif ticker == "EUR":

        buy_price = 90.00
        sell_price = 91.00

    else:

        buy_price = 0.0
        sell_price = 0.0

    spread = sell_price - buy_price

    return buy_price, sell_price, spread


buy, sell, spread = get_market_rates("USD")

print("Buy Price:", buy)
print("Sell Price:", sell)
print("Spread:", spread)


# Ignoring sell price using _
buy, _, spread = get_market_rates("EUR")

print("\nUsing underscore (_) to ignore Sell Price")
print("Buy Price:", buy)
print("Spread:", spread)