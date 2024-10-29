width = int(input())
length = int(input())
height = int(input())
cubic_meters_total = width * length * height
command = input()
total_cubic_meters = 0
free_space = True

while command != "Done":
    number_of_boxes = int(command)
    total_cubic_meters += number_of_boxes
    if total_cubic_meters >= cubic_meters_total:
        free_space = False
        break
    command = input()

diff = abs(cubic_meters_total - total_cubic_meters)
if free_space:
    print(f"{diff} Cubic meters left.")
else:
    print(f"No more free space! You need {diff} Cubic meters more.")