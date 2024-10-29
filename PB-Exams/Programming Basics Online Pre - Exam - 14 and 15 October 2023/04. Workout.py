from math import ceil

number_of_days = int(input())
kilometers = float(input())
current_kilo = kilometers
total_kilo = kilometers

for days in range(number_of_days):
    percent = int(input())
    current_kilo += (current_kilo * percent) / 100
    total_kilo += current_kilo

diff = abs(1000 - total_kilo)
if total_kilo >= 1000:
    print(f"You've done a great job running {ceil(diff)} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff)} more kilometers")