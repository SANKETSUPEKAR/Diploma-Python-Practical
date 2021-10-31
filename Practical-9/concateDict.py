dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
result = {}
for x, y in dic1.items(): result[x] = y
for x, y in dic2.items(): result[x] = y
for x, y in dic3.items(): result[x] = y
print(result)
