budget = int(input())
price = 0

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    total_price = int(command)

    if total_price + price > budget:
        print("You went in overdraft!")
        break

    price += total_price
