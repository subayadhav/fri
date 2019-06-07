h1=int(input())
l=list(map(int,input().split()))
y=0
for i in l:
    if i<0:
        y=y+i
print(y)
