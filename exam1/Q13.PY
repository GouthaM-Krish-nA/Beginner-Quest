n=int(input())
a=[]
t=int(input())
l=list(map(int,input().split()))

for i in l:
    if i not  in a:
        a.append(i)
print(a)
