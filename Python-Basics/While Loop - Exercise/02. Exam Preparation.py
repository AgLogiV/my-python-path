number_of_unsatisfactory_grades = int(input())
average_score = 0
number_of_problems = 0
last_problem = ""
total_fails = 0
failed = False
task_name = input()

while task_name != 'Enough':
    grades = int(input())
    if grades <= 4:
        total_fails += 1
        if total_fails == number_of_unsatisfactory_grades:
            failed = True
            break
    average_score += grades
    number_of_problems += 1
    last_problem = task_name
    task_name = input()

if failed:
    print(f'You need a break, {total_fails} poor grades.')
else:
    average_score /= number_of_problems
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {last_problem}')
