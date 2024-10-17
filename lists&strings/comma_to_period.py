s=input()
a=''
for i in s:
    if i==',':
        a=a+'.' 
    elif i=='.':
        a=a+','
    else:
        a=a+i
print(a)
