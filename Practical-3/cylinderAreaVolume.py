# 6. Write a program to calculate surface volume and area of a cylinder.
r = int(input("Enter Radius Of Cylinder :-"))
h = int(input("Enter Height Of Cylinder :-"))
pi = 3.14
print("Volume =", pi * r ** 2 * h, "Area =", 2 * pi * r ** 2 + 2 * pi * r * h)
