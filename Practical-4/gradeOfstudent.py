# 6. Write a program that takes the marks of 5 subjects and displays the grade.
print("Enter Marks")
math, sci, eng = int(input("Math :-")), int(input("Sci :-")), int(input("Eng :-"))
his, hin = int(input("History :-")), int(input("Hindi :-"))
marks = (math + sci + eng + his + hin) / 5
if marks < 35:
    print("Fail")
elif marks >= 35 and marks <= 50:
    print("C grade")
elif marks > 50 and marks < 80:
    print("B grade")
elif marks >= 80 and marks >= 100:
    print("A grade")
else:
    print("Don't be a oversmart please enter your proper marks...")
