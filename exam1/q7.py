n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
s=[]
sumodd=0
sumven=0
a.extend(b)
s=a.copy()
s.sort()
print(s)
for i in range(len(s)):
    if s[i]%2==0:
        sumven+=i
    else:
        sumodd+=i
print(sumven)
print(sumodd)
