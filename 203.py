n1=int(raw_input())
d={}
v=["a","e","i","o","u","A","E","I","O","U"]
for i in range(n1):
  s1=raw_input()
  c=0
  for i in s1:
    if i in v:
      c+=1
  d[s1]=c
for i in (sorted(d.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)):
  print(i[0])
