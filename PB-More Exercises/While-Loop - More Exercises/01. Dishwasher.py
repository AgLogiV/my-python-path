number_of_detergent_bottles = int(input())
total_detergent_ml = number_of_detergent_bottles * 750
command = input()
total_washed_dishes = 0
total_washed_pots = 0
charge = 0
not_enough_detergent = False

while command != "End":
    number_of_dishes = int(command)
    charge += 1
    if charge % 3 == 0:
        total_washed_pots += number_of_dishes
        detergent_ml = number_of_dishes * 15
        total_detergent_ml -= detergent_ml
    else:
        total_washed_dishes += number_of_dishes
        detergent_ml = number_of_dishes * 5
        total_detergent_ml -= detergent_ml
    if total_detergent_ml < 0:
        not_enough_detergent = True
        break
    command = input()

if not_enough_detergent:
    print(f"Not enough detergent, {abs(total_detergent_ml)} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{total_washed_dishes} dishes and {total_washed_pots} pots were washed.")
    print(f"Leftover detergent {total_detergent_ml} ml.")

