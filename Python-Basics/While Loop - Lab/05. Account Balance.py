account_deposit = 0

while True:
    text = input()

    if text == "NoMoreMoney":
        print(f'Total: {account_deposit:.2f}')
        break

    deposit_money = float(text)

    if deposit_money < 0:
        print('Invalid operation!')
        print(f'Total: {account_deposit:.2f}')
        break

    account_deposit += deposit_money
    print(f'Increase: {deposit_money:.2f}')