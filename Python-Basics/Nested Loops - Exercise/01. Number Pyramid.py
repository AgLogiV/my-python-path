number = int(input())
counter = 1
all_numbers_printed = False

for row in range(1, number + 1):
    for column in range(row):
        print(counter, end=" ")
        counter += 1
        if counter > number:
            all_numbers_printed = True
            break
    if all_numbers_printed:
        break
    print()