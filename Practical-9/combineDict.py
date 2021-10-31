d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
result = {}
for x, y in d1.items():
    result[x] = y
for x, y in d2.items():
    if x in result.keys():
        result[x] += y
    else:
        result[x] = y
print(result)
