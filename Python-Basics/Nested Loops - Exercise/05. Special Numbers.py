number = int(input())

for special in range(1111, 9999 + 1):
    current_special = str(special)
    current_number_working = True
    for digit in current_special:
        if int(digit) == 0 or number % int(digit) != 0:
            current_number_working = False
            break
    if current_number_working:
        print(current_special, end=" ")
