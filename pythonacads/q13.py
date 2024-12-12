p=input()
s=input().split()
if len(p)!=len(s):
    print(False)
else:
    d={}
    c={}
    for i,j in zip(p,s):
        if i in d:
            if d[i]!=j:
                print(False)
                break
        else:
            d[i]=j
        if j in c:
            if c[j]!=i:
                print(False)
                break
        else:
            c[j]=i
    else:
        print(True)


                
