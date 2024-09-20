n=int(input())
l=list(map(int,input().split()))
l1=l.copy()
l1.sort()
l.sort()
l.reverse()
s=[]
for i in range(n):
    s.append(l1[i])
    s.append(l[i])
print(s[0:n])


