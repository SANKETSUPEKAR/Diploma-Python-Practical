t = (11, 11, 22, 3, 21, 4, 4, 5, 32)
r = ()
for x in t:
    if t.count(x) >= 2 and x not in r:
       r += (x,)
print(r)
