n=int(input())
l=list(map(int,input().split()))
s=[]
k=[]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if (l[i]+l[j]+l[k])==0:
                s.append(l[i])
                s.append(l[j])
                s.append(l[k])
                k.append(s)
for p in range(n):
    print(s)
    
                  
print(s)
              

                
            

