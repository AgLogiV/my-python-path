import math

processors_to_do = int(input())
people = int(input())
days = int(input())

hours = people * days * 8
count_processors = math.floor(hours / 3)
money = 110.10


diff = abs(processors_to_do - count_processors)
if processors_to_do <= count_processors:
    profit = diff * money
    print(f"Profit: -> {profit:.2f} BGN")

else:
    losses = diff * money
    print(f"Losses: -> {losses:.2f} BGN")