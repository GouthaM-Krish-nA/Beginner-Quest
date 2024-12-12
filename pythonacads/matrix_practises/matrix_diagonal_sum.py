row=int(input())
col=int(input())
mat=[]
diagonal1=[]
sum2=0
for i in range(row):
  p=[]
  for j in range(col):
    n=int(input("enter the element:"))
    p.append(n)
  mat.append(p)
diagonal1=[mat[i][i] for i in range(row)]
for i in range(row):
  for j in range(col):
    if i+j==row-1 and i!=j:
      sum2+=mat[i][j]
print(sum(diagonal1)+sum2)

