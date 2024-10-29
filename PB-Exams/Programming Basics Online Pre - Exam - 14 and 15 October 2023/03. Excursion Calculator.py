number_of_people = int(input())
season = input()
price = 0

if number_of_people <= 5:
    if season == "spring":
        price = 50 * number_of_people
    elif season == "summer":
        price = 48.50 * number_of_people
        price -= price * 0.15
    elif season == "autumn":
        price = 60 * number_of_people
    elif season == "winter":
        price = 86 * number_of_people
        price += price * 0.08
elif number_of_people > 5:
    if season == "spring":
        price = 48 * number_of_people
    elif season == "summer":
        price = 45 * number_of_people
        price -= price * 0.15
    elif season == "autumn":
        price = 49.5 * number_of_people
    elif season == "winter":
        price = 85 * number_of_people
        price += price * 0.08

print(f"{price:.2f} leva.")