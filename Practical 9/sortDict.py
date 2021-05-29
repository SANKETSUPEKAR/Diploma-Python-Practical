d = {1: "C", 3: "B", 2: "G", 5: "D", 6: "A", 4: "E"}
k = list(d.keys())
v = list(d.values())
sortedDict = {}
for x in sorted(d.values()): sortedDict[k[v.index(x)]] = x
print("Ascending Order :", sortedDict)
sortedDict.clear()
for x in sorted(d.values(), reverse=True): sortedDict[k[v.index(x)]] = x
print("Descending Order :", sortedDict)
