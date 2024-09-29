#prime numbers in dictionary
n=int(input())
count=0
keys=[]
values=[]
i=2
while count!=n:
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            count+=1
            values.append(i)
            keys.append(count)
        i+=1
d=dict(zip(keys, values))
print(d)           


