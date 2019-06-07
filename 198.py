n1=int(input())
l=[int(i) for i in input().split()]
m=max(l)
mi=min(l)
print(abs(l.index(m)-l.index(mi)))
