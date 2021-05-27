# 4. Write a program to check if the input year is a leap year of not

yearInput = int(input("Enter year :-"))
if (len(str(yearInput)) == 4):
    print(yearInput, " Is Leap year") if (yearInput % 4 == 0) and (yearInput % 4 == 0) \
        else print(yearInput, " Is Not Leap year")
else:
    print("Enter Four digit year")
