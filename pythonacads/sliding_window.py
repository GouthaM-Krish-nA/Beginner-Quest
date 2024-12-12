k=int(input())
n=int(input())
p=[]
l=list(map(int,input().split()))
for i in range(n+3):

  if i+2==n:
    break
  else:
    m=max(l[i] ,l[i+1], l[i+2])
    p.append(m)
print(p)
