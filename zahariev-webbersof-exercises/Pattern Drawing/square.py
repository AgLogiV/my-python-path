number = int(input())

for i in range(1, number + 1):
    if i == 1 or i == number:
        print(f'*' * number, end="")
    elif 1 < i < number:
        print('*' + ' ' * (number - 2) + '*', end="")
    print()