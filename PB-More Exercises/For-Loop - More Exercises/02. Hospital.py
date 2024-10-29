period = int(input())

examined_patients = 0
unexamined_patients = 0
doctors = 7

for number in range(1, period + 1):
    number_of_patients = int(input())

    if number % 3 == 0 and unexamined_patients > examined_patients:
        doctors += 1

    if number_of_patients <= doctors:
        examined_patients += number_of_patients

    else:
        examined_patients += doctors
        unexamined_patients += number_of_patients - doctors

print(f"Treated patients: {examined_patients}.")
print(f"Untreated patients: {unexamined_patients}.")










