pocket_money_per_day = float(input())
earn_money_per_day = float(input())
expenses_for_entire_period = float(input())
price_of_gift = float(input())
days_left = 5

pocket_money_saved = days_left * pocket_money_per_day
earned_money = days_left * earn_money_per_day
total_money_saved = pocket_money_saved + earned_money
subtract_the_costs = total_money_saved - expenses_for_entire_period

if subtract_the_costs >= price_of_gift:
    print(f"Profit: {subtract_the_costs:.2f} BGN, the gift has been purchased.")
else:
    diff = abs(price_of_gift - subtract_the_costs)
    print(f"Insufficient money: {diff:.2f} BGN.")

