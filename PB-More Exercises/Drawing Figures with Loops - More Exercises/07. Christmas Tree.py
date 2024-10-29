number = int(input())

for side in range(0, number + 1):
    if side == 0:
        print((number - side) * " " + side * "*" + " | " + side * "*" + " " * (number + side))
    elif side != 0:
        print((number - side) * " " + side * "*" + " | " + side * "*" + " " * (number + side))
