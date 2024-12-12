n=int(input())
ce=0
co=0
for i in str(n):
  if int(i)%2==0:
    ce+=1
  else:
    co+=1
if co>0 and ce>0:
  n=ce
  #proceed
elif co==0 and ce==0:
  print("no odd no even")
elif co>0 and ce==0:
  print("no even numbers")
else:
  print("no odd numbers")



      
      
    
      
