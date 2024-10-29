number_of_students = int(input())

total_grades = 0
two = 0
three = 0
four = 0
five = 0

for student in range(1, number_of_students + 1):
    exam_grade = float(input())
    total_grades += exam_grade

    if 2.00 <= exam_grade <= 2.99:
        two += 1

    elif 3.00 <= exam_grade <= 3.99:
        three += 1

    elif 4.00 <= exam_grade <= 4.99:
        four += 1

    elif exam_grade >= 5.00:
        five += 1

top_students = (five * 100) / number_of_students
between_four = (four * 100) / number_of_students
between_three = (three * 100) / number_of_students
between_two = (two * 100) / number_of_students
average_grades = total_grades / number_of_students

print(f"Top students: {top_students: .2f}%")
print(f"Between 4.00 and 4.99: {between_four: .2f}%")
print(f"Between 3.00 and 3.99: {between_three: .2f}%")
print(f"Fail: {between_two: .2f}%")
print(f"Average: {average_grades: .2f}")
