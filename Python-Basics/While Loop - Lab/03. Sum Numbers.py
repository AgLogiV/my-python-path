# number = int(input())
#
# total_sum = 0
#
# while True:
#     num = int(input())
#     total_sum += num
#
#     if total_sum >= number:
#         print(total_sum)
#         break
#
#     continue


number = int(input())

total_sum = 0

while total_sum < number:
    num = int(input())
    total_sum += num

print(total_sum)
