row=int(input())
col=int(input())
mat=[]
nrow=int(input())
ncol=int(input())
for i in range(row):
  p=[]
  for j in range(col):
    n=int(input("enter the element:"))
    p.append(n)
  mat.append(p)
# the approach is to check if the row*column product is same for the new and the old matrix
# then we just take all the elements of the list to a single list and pass into the reshaped matrix easy!!
if row*col != nrow*ncol:
  print("invalid input")
else:
  x=[mat[i][j] for i in range(row) for j in range(col)]
  new_mat=[[0]*ncol for i in range(nrow)]
  k=0
  for i in range(nrow):
    for j in range(ncol):
      new_mat[i][j]=x[k]
      k+=1
print(new_mat)


    
