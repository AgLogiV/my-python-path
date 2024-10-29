number = float(input())

if number == 0:
    print('zero')
# Small/Large Positive
elif 1 > number > 0:
    print('small positive')
elif 1 <= number <= 1000000:
    print('positive')
elif number > 1000000:
    print('large positive')
# Small/Large Negative
elif -1 < number < 0:
    print('small negative')
elif -1 >= number >= -1000000:
    print('negative')
elif number < -1000000:
    print('large negative')

# Вариант 2:

number = float(input())

if number == 0:
    print('zero')

elif number > 0:
    if number < 1:
        print('small positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('positive')

elif number < 0:
    if number > -1:
        print('small negative')
    elif number < -1000000:
        print('large negative')
    else:
        print('negative')

# Вариант 3

number = float(input())

if number == 0:
    print('zero')

elif number > 0:
    if number < 1:
        print('small positive')
    elif number > 1000000:
        print('large positive')
    else:
        print('positive')

elif number < 0:
    if abs(number) < 1:
        print('small negative')
    elif abs(number) > 1000000:
        print('large negative')
    else:
        print('negative')
