upper_limit_of_first_number = int(input())
upper_limit_of_second_number = int(input())
upper_limit_of_third_number = int(input())

for first_limit in range(1, upper_limit_of_first_number + 1):
    for second_limit in range(1, upper_limit_of_second_number + 1):
        for third_limit in range(1, upper_limit_of_third_number + 1):
            if first_limit % 2 == 0 and third_limit % 2 == 0 and str(second_limit) in "2357":
                print(f"{first_limit} {second_limit} {third_limit}")

