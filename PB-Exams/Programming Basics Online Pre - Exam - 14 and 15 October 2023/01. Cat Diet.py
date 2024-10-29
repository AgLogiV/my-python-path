fat_percentage = int(input())
percentage_of_proteins = int(input())
percentage_of_carbohydrates = int(input())
total_calories = int(input())
percentage_of_water_content = int(input())

total_fat_grams = (total_calories * (fat_percentage / 100)) / 9
total_grams_of_protein = (total_calories * (percentage_of_proteins / 100)) / 4
total_grams_of_carbohydrates = (total_calories * (percentage_of_carbohydrates / 100)) / 4

weight_of_food = total_fat_grams + total_grams_of_protein + total_grams_of_carbohydrates
calories_per_gram_of_food = total_calories / weight_of_food
remaining_percentages = (100 - percentage_of_water_content) / 100
in_one_gram_of_this_type_of_food_there_is = calories_per_gram_of_food * remaining_percentages

print(f'{in_one_gram_of_this_type_of_food_there_is:.4f}')