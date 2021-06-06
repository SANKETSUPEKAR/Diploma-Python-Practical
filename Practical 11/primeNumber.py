def prime(num):
    temp = True
    for i in range(2, num):
        if num % i == 0:
            temp = False
            break
    if temp:
        print("Number Is Prime")
    else:
        print("Number Is Not Prime")


prime(int(input("Enter Number : ")))
