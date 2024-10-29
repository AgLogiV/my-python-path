n = int(input())
forbidden_charts = ',._'

for symbols in range(n):
    word = input()
    not_pure = False
    for symbol in forbidden_charts:
        if symbol in word:
            not_pure = True
    if not_pure:
        print(f"{word} is not pure!")
    else:
        print(f"{word} is pure.")