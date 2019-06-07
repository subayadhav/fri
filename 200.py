s1=input()
l=[]
a=""
for i in s1:
	if s1.count(i)!=1 and i not in l:
		l.append(i)
		a=a+i
	elif s1.count(i)==1:
		a=a+i
print(a)
