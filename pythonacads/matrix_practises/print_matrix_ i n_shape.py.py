row=int(input())
col=int(input())
mat=[]
for i in range(row):
  n=list(map(int,input("enter the element:").split()))
  mat.append(n)
for i in mat:
  print('[', *i ,']')