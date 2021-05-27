n1 = 0
n2 = 1
for i in range(0, 20):
    fib = n1 + n2
    print(fib)
    n1 = n2
    n2 = fib
