d = {1: "C", 3: "B", 2: "G", 5: "D", 6: "A", 4: "E"}
sortedDict = {}

for x in sorted(d.values()):
    for k, v in d.items():
        if x == v:
            sortedDict[k] = v
print("Ascending Order :", sortedDict)
sortedDict.clear()

for x in sorted(d.values(), reverse=True):
    for k, v in d.items():
        if x == v:
            sortedDict[k] = v
print("Descending Order :", sortedDict)
