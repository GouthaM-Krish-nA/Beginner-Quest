row=int(input())
col=int(input())
mat=[]
diagonals=[]
for i in range(row):
  p=[]
  for j in range(col):
    n=int(input("enter the element:"))
    p.append(n)
  mat.append(p)
for r in range(row-1,-1,-1): #or just in range(row):
  diagonal=[]
  i=r
  j=0
  while i<row and j<col :
    diagonal.append(mat[i][j])
    i+=1
    j+=1
  diagonals.append(diagonal)
for c in range(1,col):
  diagonal=[]
  i=0
  j=c
  while i<row and j<col:
    diagonal.append(mat[i][j])
    i+=1
    j+=1
  diagonals.append(diagonal)
print(diagonals)