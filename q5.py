n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
s = []

if m > n:
    for i in range(n):
        s.append(a[i])
        s.append(b[i])
    
    
    s.extend(b[n:])
else:
    for i in range(m):
        s.append(a[i])
        s.append(b[i])
    
    
    s.extend(a[m:])


print(s)
