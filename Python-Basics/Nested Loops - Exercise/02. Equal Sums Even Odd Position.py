first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    current_number_in_str = str(current_number)
    even_number_count = 0
    odd_number_count = 0
    for index, digit in enumerate(current_number_in_str):
        current_digit = int(digit)
        if index % 2 == 0:
            odd_number_count += current_digit
        elif index % 2 != 0:
            even_number_count += current_digit
    if even_number_count == odd_number_count:
        print(current_number, end=" ")