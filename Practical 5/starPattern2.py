# a. Print the Star Diamond patterns using loop:
num = 6
for i in range(1, num, 2):
    print(" " * ((num - i) // 2), end='')
    print("*" * i)
for j in reversed(range(1, num - 1, 2)):
    print(" " * ((num - j) // 2), end='')
    print("*" * j)
