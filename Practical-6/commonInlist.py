# 6. Write a Python program to find common items from two lists.
list1 = [10, 20, 30, 40, 50]
list2 = [2, 10, 15, 20, 25]
print([x for x in list1 for y in list2 if x == y])
