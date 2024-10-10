n=int(input())
l=list(map(int,input().split()))
sum=0
p=[]
for i in range(n):
    sum=sum+l[i]
    p.append(sum)
print(p)    