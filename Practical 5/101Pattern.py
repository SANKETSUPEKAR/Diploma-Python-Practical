num = 4
for i in reversed(range(0, num)):
    for k in range(0, num - i):
        print(" ", end=''),
    for j in range(0, i):
        print(1, end=''),
        print(0, end=''),
    print(1)
