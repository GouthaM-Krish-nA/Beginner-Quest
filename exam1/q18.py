n=int(input())
d={}
s,p=[],[1,2,3]
c1,c2,c3=0,0,0
for i in range(n):
    k=int(input())
    s.append(k)

for i in s:
    if i==1:
        c1+=1
    elif i==2:
        c2+=1
    else:
        c3+=1
q=[c1,c2,c3]
print(dict(zip(p, q)))