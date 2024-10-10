n=int(input())
l=list(map(int,input().split()))
t=int(input())
p=[]
for i in range(len(l)):
    if l[i]>t:
        p.append(l[i])
        
if not p:
    print("No ages exceed the threshold")
else:
    print(p)
