num = str(input("Enter Number  :- "))
num2 = ""
for i in reversed(num):
    num2 += i
print("Number is Palindrome") if num == num2 else print("Number is Not Palindrome")
