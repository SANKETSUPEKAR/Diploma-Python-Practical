list = [int(test) for test in input("Enter Test Marks 1 2 3 Respectively : ").split()]
list.sort(reverse=True)
print("Best of two test average marks = ", (list[0] + list[1]) / 2, "%")
