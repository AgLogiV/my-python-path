prime_numbers_sum = 0
non_prime_numbers_sum = 0
command = input()

while command != "stop":
    current_number = int(command)
    number_is_prime = True
    if current_number < 0:
        print("Number is negative.")
    else:
        for number in range(2, current_number):
            if current_number == 0 or current_number % number == 0:
                non_prime_numbers_sum += current_number
                break
        else:
            prime_numbers_sum += current_number
    command = input()

print(f"Sum of all prime numbers is: {prime_numbers_sum}")
print(f"Sum of all non prime numbers is: {non_prime_numbers_sum}")