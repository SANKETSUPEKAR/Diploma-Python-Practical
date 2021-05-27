# 5. Write a Python program to calculate factorial of a number
num = int(input("Enter Number :"))
fact = 1
for i in range(0, num):
    fact = fact * (num - i)
print(fact)
