sl=str(input())
s=sl[::-1]
m=""
for i in s:
    a=s.index(i)
    if i=='/':
        n=s[a+1:]
        print(n[::-1])
        break
for j in s:
    a=s.index(j)
    if j=='-':
        print(m[::-1])
        break
    else:
        m=m+j



    