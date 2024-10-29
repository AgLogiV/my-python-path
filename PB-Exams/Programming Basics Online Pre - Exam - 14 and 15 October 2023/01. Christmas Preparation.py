number_rolls_of_wrapping_paper = int(input())
number_fabric_rolls = int(input())
liters_of_glue = float(input())
percentage_reduction = int(input())

price_of_rolls_of_paper = number_rolls_of_wrapping_paper * 5.8
price_of_fabric_rolls = number_fabric_rolls * 7.2
glue_price = liters_of_glue * 1.2
price_for_all_materials = price_of_rolls_of_paper + price_of_fabric_rolls + glue_price
price_with_discount = price_for_all_materials - (price_for_all_materials * (percentage_reduction / 100))

print(f'{price_with_discount:.3f}')
