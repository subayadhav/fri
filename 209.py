n1=int(input())
l=[]
s=1
k=1
for i in range(0,n1):
    l.append(list(map(int,input().split())))
for i in range(0,n1):
    for j in range(0,n1):
        if i==j:
            s=s*l[i][j]
        if i+j==n1-1:
            k=k*l[i][j]
print(s+k)
