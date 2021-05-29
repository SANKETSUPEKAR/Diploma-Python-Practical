data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
        {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
result = []
for x in data:
    result.append(list(x.values()))
for x in result:
    if result.count(x) < 2:
        print(x)
