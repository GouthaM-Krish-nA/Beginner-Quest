row=int(input())
col=int(input())
mat=[]
for i in range(row):
  p=[]
  for j in range(col):
    n=int(input("enter the element:"))
    p.append(n)
  mat.append(p)
mx=[max(col) for col in zip(*mat)]
for i in range(row):
  for j in range(col):
    if mat[i][j]==-1:
      mat[i][j]=mx[j]
print(mat)
