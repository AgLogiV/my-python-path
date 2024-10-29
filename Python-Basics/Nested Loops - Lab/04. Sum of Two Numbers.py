start_interval = int(input())
last_interval = int(input())
magic_number = int(input())
combination_counter = 0
combination_founded = False
text = ""

for num1 in range(start_interval, last_interval + 1):
    for num2 in range(start_interval, last_interval + 1):
        combination_counter += 1
        if num1 + num2 == magic_number:
            combination_founded = True
            text = f"Combination N:{combination_counter} ({num1} + {num2} = {magic_number})"
            break
    if combination_founded:
        break

if combination_founded:
    print(text)
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")