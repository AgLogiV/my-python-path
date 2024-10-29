import sys

max_num = -sys.maxsize

while True:
    text = input()

    if text == "Stop":
        print(max_num)
        break

    number = int(text)

    if number > max_num:
        max_num = number
