student_name = input()

total_grades = 0
current_class = 0
total_fails = 0

while current_class < 12:
    grades = float(input())

    if grades < 4:
        total_fails += 1
        if total_fails > 1:
            print(f'{student_name} has been excluded at {current_class + 1} grade')
            break
        continue

    current_class += 1
    total_grades += grades

else:
    print(f'{student_name} graduated. Average grade: {total_grades / current_class: .2f}')
