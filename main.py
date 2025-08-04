# Dictionary to store stock prices (manually defined)
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350,
    "AMZN": 145
}

# Dictionary to store user's portfolio
portfolio = {}

print("STOCK PORTFOLIO TRACKER")
print("Available stocks:", list(stock_prices.keys()))
print()

while True:
    print("type 'done' to finish")
    stock = input("Enter stock symbol: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Available stocks:", list(stock_prices.keys()))
        continue

    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        print("\n")
        if quantity <= 0:
            print("Quantity must be positive!")
            continue
        portfolio[stock] = quantity
    except ValueError:
        print("Please enter a valid number!")
        continue

# Calculate and display portfolio
if not portfolio:
    print("No stocks in portfolio!")
else:
    print("\n" + "=" * 40)
    print("YOUR PORTFOLIO")
    print("=" * 40)

    total_value = 0

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        value = quantity * price
        total_value += value

        print(f"{stock}: {quantity} shares @ ${price} = ${value}")

    print("-" * 40)
    print(f"TOTAL PORTFOLIO VALUE: ${total_value}")
    print("=" * 40)

    # Optional: Save to file
    save = input("\nSave results to file? (y/n): ").lower()

    if save == 'y':
        filename = input("Enter filename (without extension): ")
        file_type = input("Save as txt or csv? ").lower()

        if file_type == "csv":
            with open(f"{filename}.csv", "w") as file:
                file.write("Stock,Quantity,Price,Value\n")
                for stock, quantity in portfolio.items():
                    price = stock_prices[stock]
                    value = quantity * price
                    file.write(f"{stock},{quantity},{price},{value}\n")
                file.write(f"Total,,,{total_value}\n")
        else:
            with open(f"{filename}.txt", "w") as file:
                file.write("STOCK PORTFOLIO TRACKER\n")
                file.write("=" * 40 + "\n")
                for stock, quantity in portfolio.items():
                    price = stock_prices[stock]
                    value = quantity * price
                    file.write(f"{stock}: {quantity} shares @ ${price} = ${value}\n")
                file.write("-" * 40 + "\n")
                file.write(f"TOTAL PORTFOLIO VALUE: ${total_value}\n")

        print(f"Portfolio saved to {filename}.{file_type}")

    print("Thank you for using Stock Portfolio Tracker!")