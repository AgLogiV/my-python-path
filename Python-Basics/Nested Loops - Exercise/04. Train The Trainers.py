number_of_jury = int(input())
presentation_name = input()
total_grades_for_all = 0
grades_counter = 0

while presentation_name != "Finish":
    total_grades = 0
    for grades in range(number_of_jury):
        current_grade = float(input())
        total_grades += current_grade
        total_grades_for_all += current_grade
        grades_counter += 1
    print(f"{presentation_name} - {total_grades / number_of_jury:.2f}.")
    presentation_name = input()

total_average_grade = total_grades_for_all / grades_counter
print(f"Student's final assessment is {total_average_grade:.2f}.")