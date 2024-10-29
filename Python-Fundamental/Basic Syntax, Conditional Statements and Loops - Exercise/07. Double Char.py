while True:
    text = input()
    if text == "End":
        break
    if text == "SoftUni":
        continue
    else:
        for character in text[0:]:
            print(character + character, end="")
    print()