n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=[]
p=[]
for i in range(n):
    if l[i]>k:
        s.append(l[i])
    else:
        p.append(l[i])
s.extend(p)
print(s)
