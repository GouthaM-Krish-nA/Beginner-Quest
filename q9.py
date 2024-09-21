n=int(input())
l=list(map(int,input().split()))
m=int(input())
s=[]
p=[]
for i in range(n):
    if l[i]<m:
        s.append(l[i])
    else:
        p.append(l[i])
print(s)    
print(p)