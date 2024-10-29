divisor = int(input())
boundary = int(input())

for largest in range(boundary, divisor - 1, -1):
    if largest % divisor == 0 and largest <= boundary:
        print(largest)
        break
