first_text = input()
second_text = input()

for index in range(len(first_text)):
    if first_text[index] != second_text[index]:
        first_text = second_text[:index + 1] + first_text[index + 1:]
        print(first_text)