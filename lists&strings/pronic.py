n=int(input())
c=0
s=[]
for i in range(1,n-1):
    for j in range(i+1,n-1):
        if (i*j==n) and ((j-i==1)or (i-j==1)):
                c+=1
                break
if (c>0):
      print("The number is pronic .yay!")
if c==0:
      print("The number is not pronic")

