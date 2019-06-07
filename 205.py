s1=input()
t=""
for i in s1:
	if i.isupper():
		t+=i.lower()
	else:
		t+=i.upper()
print(t)
