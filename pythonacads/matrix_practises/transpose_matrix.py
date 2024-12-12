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
# check how the elements are changing from their initial to final position
#from old (i,j) to new (i,j)
#now for this question create an empty matrix using this list comprehension
# new_mat=[[0]*coloums for i in range(rows)] this should be the actual one but since we are transposing matrix the row and col number gets interchanged
new_mat=[[0]*row for i in range(col)]  #initialize an empty matrix
for i in range(row):
  for j in range(col):
    new_mat[j][i] = mat[i][j]
print(new_mat)




















# def transpose(mat):
#     m = len(mat)  # Number of rows
#     n = len(mat[0])  # Number of columns
    
#     # Initialize an empty result matrix with dimensions n x m
#     result = [[0] * m for _ in range(n)]
    
#     # Populate the result matrix
#     for i in range(m):
#         for j in range(n):
#             result[j][i] = mat[i][j]  # Swap rows with columns
    
#     return result

