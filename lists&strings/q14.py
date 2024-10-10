m=int(input())
#nothing to do with dictionary
d={}
keys=[]
values=[]
for i in range(m):
    sid=int(input())
    temp=int(input())
    d[sid]=temp
    keys.append(sid)
    values.append(temp)
mi=min(d, key=d.get)
 #mi=values.index(min(values))
print(mi)
