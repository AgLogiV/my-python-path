n = int(input())
n_one = int(input())
n_two = int(input())

current_sum = n_one + n_two
current_diff = 0
check = True

for num in range(n - 1):
    n_one = int(input())
    n_two = int(input())
    current = n_one + n_two

    if current != current_sum:
        diff = abs(current - current_sum)
        if diff > current_diff:
            current_diff = diff
        current_sum = current
        check = False

if check:
    print(f'Yes, value={current_sum}')
else:
    print(f"No, maxdiff={current_diff}")