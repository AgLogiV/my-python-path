number = int(input())

for row in range(1, number + 1):
    if row == 1:
        print((number - row) * " " + row * "*")
    else:
        print((number - row) * " " + row * "* ")

for rows in range(number - 1):
    if rows == number:
        print((number - rows) * " " + (number - 1) * "* ")
    else:
        print((rows + 1) * " " + (number - rows - 1) * "* ")