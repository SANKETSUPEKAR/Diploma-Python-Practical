def cal(s):
    u = 0
    l = 0
    for i in s:
        if i.isupper():
            u += 1
        if i.islower():
            l += 1
    print("Number Of Upper Case {0} \nNumber Of Lower Case {1}".format(u, l))


cal(input("Enter String : "))
