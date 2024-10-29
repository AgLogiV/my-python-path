word = input()

print(word[::-1])

# Вариант 2
word = input()

for i in range(len(word) -1, -1, -1):
    print(word[i], end="")

#Вариант 3
word = input()

for char in word[::-1]:
    print(char, end='')