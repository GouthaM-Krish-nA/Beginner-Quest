s=str(input())
a=""
b=""
c=""
count=0
for i in s:
  a=s[0:5]
  b=s[5:9]
  c=s[-1]
if a.isupper() and a.isalpha() :
  count+=1
if b.isdigit():
  count+=1
if c.isupper() and c.isalpha() :
  count+=1
if count==3:
  print('VALID')
else:
  print("INVALID")
print(count)