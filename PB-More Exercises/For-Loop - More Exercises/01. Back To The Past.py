inherited_money = float(input())
year_to_live_up_to = int(input())

total_money = inherited_money
age = 18

for year in range(1800, year_to_live_up_to + 1):
    if year % 2 == 0:
        total_money -= 12000

    else:
        total_money -= 12000 + age * 50
    age += 1

if total_money >= 0:
    print(f"Yes! He will live a carefree life and will have {total_money:.2f} dollars left.")
else:
    print(f"He will need {abs(total_money):.2f} dollars to survive.")