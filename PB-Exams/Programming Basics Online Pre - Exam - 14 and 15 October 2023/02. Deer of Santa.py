import math

number_of_days = int(input())
food_left_kilograms = int(input())
food_per_day_for_first_deer_kilograms = float(input())
food_per_day_for_second_deer_kilograms = float(input())
food_per_day_for_third_deer_kilograms = float(input())

first_deer = number_of_days * food_per_day_for_first_deer_kilograms
second_deer = number_of_days * food_per_day_for_second_deer_kilograms
third_deer = number_of_days * food_per_day_for_third_deer_kilograms

total_needed_food = first_deer + second_deer + third_deer

diff = abs(food_left_kilograms - total_needed_food)
if total_needed_food <= food_left_kilograms:
    print(f'{math.floor(diff)} kilos of food left.')
else:
    print(f'{math.ceil(diff)} more kilos of food are needed.')
