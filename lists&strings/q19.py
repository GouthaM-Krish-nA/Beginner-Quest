n=int((input()))
d1,d2={},{}
for i in range(n):
    keys=int(input())
    values=int(input())
    d1[keys]=values
m=int(input())
for i in range(m):
    keys=int(input())
    values=int(input())
    d2[keys]=values
    if keys in d1:
        d1[keys]+=values
    else:
        d1[keys]=values
print(d1)


