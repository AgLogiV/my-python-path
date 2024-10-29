months = int(input())

electricity = 0
water = 20
internet = 15
others = 0

for price in range(months):
    electricity_bill = float(input())
    electricity += electricity_bill
    others += (electricity_bill + water + internet) + (electricity_bill + water + internet) * 0.20

total_water = months * water
total_internet = months * internet
average_for_month = (electricity + total_water + total_internet + others) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average_for_month:.2f} lv")