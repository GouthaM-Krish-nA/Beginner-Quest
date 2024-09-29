n=int(input())
d={}

for i in range(n):
    key1=int(input())
    value1=int(input())
    d[key1]=value1
inv={value1:key1 for key1,value1 in d.items()}
for key,value in inv.items():
    print(key,":", value)
    