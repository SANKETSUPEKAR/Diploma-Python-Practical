# 5. Write a program to check if a Number is Positive, Negative or Zero
num = (int(input("Enter Number :-")))
print(num, " Is Zero") if num == 0 else (print(num, " Is Positive") if (num > 0) else print(num, " Is Negative"))
