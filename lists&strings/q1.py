n=int(input())
l=list(map(int,input().split()))
l.pop(0)
l.pop()
for i in range(len(l)):#dont use range as n beacuse list elemnt no is modified
    if (l[i])%2==0:
        l[i]=l[i]-3
    else:
        l[i]=l[i]*2
print(l)
