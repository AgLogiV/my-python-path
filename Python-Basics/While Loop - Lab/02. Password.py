# name = input()
# password = input()
#
# while True:
#     data = input()
#
#     if data == password:
#         print(f'Welcome {name}!')
#         break
#
#     continue

name = input()
password = input()

data = input()

while data != password:
    data = input()

print(f'Welcome {name}!')
