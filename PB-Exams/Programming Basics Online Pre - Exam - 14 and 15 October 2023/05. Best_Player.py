import sys

player_name = ""
last_player_goals = -sys.maxsize

while True:
    command = input()
    if command == "END":
        break
    number_of_goals = int(input())
    if number_of_goals > last_player_goals:
        player_name = command
        last_player_goals = number_of_goals
    if number_of_goals >= 10:
        break

if last_player_goals >= 3:
    print(f"{player_name} is the best player!")
    print(f"He has scored {last_player_goals} goals and made a hat-trick !!!")
else:
    print(f"{player_name} is the best player!")
    print(f"He has scored {last_player_goals} goals.")
