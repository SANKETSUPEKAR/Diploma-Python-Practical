d = {'a': 200, 'b': 100, 'c': 300, 'd': 50, 'e': 600}
for x in range(3):
    print(sorted(d.values(), reverse=True)[x])
