

while True:
    n = float(input())

    if n < 0:
        print('Negative number!')
        break

    result = n * 2
    print(f'Result: {result:.2f}')