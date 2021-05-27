# 3. Write a program to check the largest number among the three numbers
a, b, c = int(input("Enter number 1 :-")), int(input("Enter number 2 :-")), int(input("Enter number 3 :-"))
if a == b == c:
    print("All Numbers are equal")
else:
    if a >= b and a >= c:
        print(a, " Is Larger")
    elif b >= a and b >= c:
        print(b, " Is Larger")
    elif c >= b and c >= a:
        print(c, " Is Larger")

    if a == b:
        print("A and B are equal")
    else:
        if a == c:
            print("A and C are equal")
        elif b == c:
            print("C and B are equal")
