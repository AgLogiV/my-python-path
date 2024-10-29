floors = int(input())
apartments = int(input())
floor_name = ""

for floor in range(floors, 0, -1):
    for rooms in range(0, apartments):
        if floor == floors:
            floor_name = f'L{floor}{rooms}'
        elif floor % 2 == 0:
            floor_name = f'O{floor}{rooms}'
        elif floor % 2 != 0:
            floor_name = f'A{floor}{rooms}'
        print(floor_name, end=" ")
    print()
