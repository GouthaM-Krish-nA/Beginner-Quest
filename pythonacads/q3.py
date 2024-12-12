l=list(map(int,input().split()))
k=int(input())
for i in range(k-1):
    l.pop(l.index(min(l)))
print(min(l))
