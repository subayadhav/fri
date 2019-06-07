s1=input()
l=['a','e','i','o','u']
a=[]
b=[]
for i in s1:
	if i in l:
		a.append(i)
	else:
		b.append(i)
print("".join(a+b))
