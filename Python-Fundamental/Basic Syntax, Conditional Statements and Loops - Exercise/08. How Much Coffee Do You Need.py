coffee_count = 0

while True:
    event = input()
    if event == "END":
        break
    if event == 'coding' or event == 'dog' or event == 'cat' or event == 'movie':
        coffee_count += 1
    elif event == 'CODING' or event == 'DOG' or event == 'CAT' or event == 'MOVIE':
        coffee_count += 2
    elif event != ['coding', 'dog', 'cat', 'movie', 'CODING', 'DOG', 'CAT', 'MOVIE']:
        continue

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)
