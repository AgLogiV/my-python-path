number_of_mans = int(input())
number_of_women = int(input())
max_tables = int(input())
table_counter = 0
tables_full = False

for num1 in range(1, number_of_mans + 1):
    for num2 in range(1, number_of_women + 1):
        print(f'({num1} <-> {num2})', end=" ")
        table_counter += 1
        if table_counter == max_tables:
            tables_full = True
            break
    if tables_full:
        break
