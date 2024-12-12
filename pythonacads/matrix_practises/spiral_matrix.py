row=int(input())
col=int(input())
m=[]
for i in range(row):
  p=[]
  for j in range(col):
    n=int(input("enter the element:"))
    p.append(n)
  m.append(p)
s=[]
def pos(a,b):
  if a<row and b<col:
    return True
  else:
    return False

i=0
j=0
while pos(i,j) and m[i][j] !=-1:
    s.append(m[i][j])
    m[i][j]=-1
    j+=1
print(i,j)
while pos(i+1,j-1) and m[i+1][j-1] !=-1:
  s.append(m[i+1][j-1])
  m[i+1][j-1]=-1
  

while pos(i-1,j-1) and m[i-1][j-1] !=-1:
  s.append(m[i-1][j-1])
  m[i-1][j-1]=-1
print(i,j)
while pos(i-1,j+1) and m[i-1][j+1]:
  s.append(m[i-1][j+1])
  m[i-1][j+1]=-1
print(s)

      






