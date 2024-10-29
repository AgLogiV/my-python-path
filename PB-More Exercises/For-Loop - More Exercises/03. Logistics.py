number_of_loads = int(input())

total_loads = 0
van = 0
truck = 0
train = 0

for loads in range(1, number_of_loads + 1):
    cargo_tonnage = int(input())
    total_loads += cargo_tonnage

    if cargo_tonnage <= 3:
        van += cargo_tonnage

    elif 4 <= cargo_tonnage <= 11:
        truck += cargo_tonnage

    elif cargo_tonnage >= 12:
        train += cargo_tonnage

total_tons = van + truck + train
average_per_ton = (van * 200 + truck * 175 + train * 120) / total_tons
with_van = van / total_tons * 100
with_truck = truck / total_tons * 100
with_train = train / total_tons * 100

print(f'{average_per_ton:.2f}')
print(f'{with_van:.2f}%')
print(f'{with_truck:.2f}%')
print(f'{with_train:.2f}%')

