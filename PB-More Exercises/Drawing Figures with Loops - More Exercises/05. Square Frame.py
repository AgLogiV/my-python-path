number = int(input())

for rectangle in range(1, number + 1):
    for figure in range(1, number + 1):
        if (figure == 1 and rectangle == 1 or figure == number and rectangle == 1 or
                figure == 1 and rectangle == number or figure == number and rectangle == number):
            print("+", end=" ")
        elif figure == 1 and rectangle != 1 or figure == number and rectangle != number:
            print("|", end=" ")
        else:
            print("-", end=" ")
    print()
