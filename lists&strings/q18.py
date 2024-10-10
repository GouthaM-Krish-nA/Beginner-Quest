n=int(input())
s,keys,values=[],[],[]
c=0
for i in range(n):
    k=int(input())
    s.append(k)

for i in s:
    c=s.count(i)
    s.remove(i)
    keys.append(i)
    values.append(c)

print(keys)
