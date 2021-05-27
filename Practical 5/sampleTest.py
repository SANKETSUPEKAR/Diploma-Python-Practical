n = int(input())
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z']
alphaList = [l[x] for x in range(n)]
w = (len(alphaList) * 2) - 1 + (len(alphaList) * 2) - 2
for x in reversed(range(1, len(alphaList))):
    a = "-".join((*reversed(alphaList[x + 1:]), *alphaList[x:]))
    print(a.center(w, "-"))
for x in range(len(alphaList)):
    a = "-".join((*reversed(alphaList[x + 1:]), *alphaList[x:]))
    print(a.center(w, "-"))
