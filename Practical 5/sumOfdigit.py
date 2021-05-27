# 7. Write a Python program takes in a number and finds the sum of digits in a number.
num = str(input("Enter Number :-"))
sum = 0
for i in num:
    sum += int(i)
print("Sum of digits", sum)
