start_letter = input()
end_letter = input()
skip_letter = input()

skip_ascii_number = ord(skip_letter)
start_ascii_number = ord(start_letter)
end_ascii_number = ord(end_letter)
combination_found = 0

for first_letter in range(start_ascii_number, end_ascii_number + 1):
    for second_letter in range(start_ascii_number, end_ascii_number + 1):
        for third_letter in range(start_ascii_number, end_ascii_number + 1):
            if first_letter != skip_ascii_number and second_letter != skip_ascii_number and third_letter != skip_ascii_number:
                combination_found += 1
                print(f'{chr(first_letter)}{chr(second_letter)}{chr(third_letter)}', end=" ")
print(combination_found)