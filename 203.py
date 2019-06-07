def count(s):
    k1=0
    for i in s:
        if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
            k1=k1+1
    return k1
n=int(input())
l=[]
for i in range(0,n):
    s=input()
    l.append([s,count(s)])
l.sort(key=lambda x:x[1],reverse=True)
for i in range(0,len(l)):
    print(l[i][0])
