s=str(input())
sum=0
for i in s:
    if i.isdigit()==True:
        sum=sum+int(i)
print(sum)