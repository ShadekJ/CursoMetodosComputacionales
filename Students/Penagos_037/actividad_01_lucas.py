#!usr/bin/env python
def lucas(n):
    l=[2,1]
    while True:
        if len(l)>=n:
            break
        l.append(l[-1]+l[-2])
    return l[:n][-1]

n=int(input("Ingrese n:\n"))
print(lucas(n))
