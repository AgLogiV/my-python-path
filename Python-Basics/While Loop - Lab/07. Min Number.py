import sys

min_num = sys.maxsize

while True:
    text = input()

    if text == "Stop":
        print(min_num)
        break

    number = int(text)

    if number < min_num:
        min_num = number
