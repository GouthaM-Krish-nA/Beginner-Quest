n=int(input())
l=list(map(int,input().split()))
p=[x for x in range(l[0],max(l)) if x not in l]
print(p)