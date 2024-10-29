move_during_game = int(input())

result = 0
row_one = 0
row_two = 0
row_three = 0
row_four = 0
row_five = 0
invalid_row = 0

for moves in range(move_during_game):
    numbers_in_moves = int(input())

    if 0 <= numbers_in_moves <= 9:
        row_one += 1
        result += numbers_in_moves * 0.20

    elif 10 <= numbers_in_moves <= 19:
        row_two += 1
        result += numbers_in_moves * 0.30

    elif 20 <= numbers_in_moves <= 29:
        row_three += 1
        result += numbers_in_moves * 0.40

    elif 30 <= numbers_in_moves <= 39:
        row_four += 1
        result += 50

    elif 40 <= numbers_in_moves <= 50:
        row_five += 1
        result += 100

    elif numbers_in_moves < 0 or numbers_in_moves > 50:
        invalid_row += 1
        result = result / 2

total_row_one = (row_one * 100) / move_during_game
total_row_two = (row_two * 100) / move_during_game
total_row_three = (row_three * 100) / move_during_game
total_row_four = (row_four * 100) / move_during_game
total_row_five = (row_five * 100) / move_during_game
total_invalid_row = (invalid_row * 100) / move_during_game

print(f'{result:.2f}')
print(f"From 0 to 9: {total_row_one:.2f}%")
print(f"From 10 to 19: {total_row_two:.2f}%")
print(f"From 20 to 29: {total_row_three:.2f}%")
print(f"From 30 to 39: {total_row_four:.2f}%")
print(f"From 40 to 50: {total_row_five:.2f}%")
print(f"Invalid numbers: {total_invalid_row:.2f}%")