amount = int(input())
command = input()
counter = 0
cash = 0
card = 0
cash_counter = 0
card_counter = 0

while command != "End":
    counter += 1
    item_prices = int(command)
    # логика за неуспешни плащания
    if item_prices < 10 and counter % 2 == 0 or item_prices > 100 and counter % 2 != 0:
        print("Error in transaction!")
    # логика за успешни плащания
    elif item_prices <= 100 and counter % 2 != 0:
        cash += item_prices
        cash_counter += 1
        print("Product sold!")
    elif item_prices > 10 and counter % 2 == 0:
        card += item_prices
        card_counter += 1
        print("Product sold!")

    # логика за ако плащанията са стигнали
    total_payment = card + cash
    if total_payment >= amount:
        print(f"Average CS: {cash / cash_counter:.2f}")
        print(f"Average CC: {card / card_counter:.2f}")
        break

    command = input()

else:
    print("Failed to collect required money for charity.")

