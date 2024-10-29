capacity_of_stadium = int(input())
number_of_all_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fan in range(number_of_all_fans):
    sector = input()

    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

total_sector_a = sector_a / number_of_all_fans * 100
total_sector_b = sector_b / number_of_all_fans * 100
total_sector_v = sector_v / number_of_all_fans * 100
total_sector_g = sector_g / number_of_all_fans * 100
total_percent_of_all_fans = number_of_all_fans / capacity_of_stadium * 100

print(f'{total_sector_a:.2f}%')
print(f'{total_sector_b:.2f}%')
print(f'{total_sector_v:.2f}%')
print(f'{total_sector_g:.2f}%')
print(f'{total_percent_of_all_fans:.2f}%')