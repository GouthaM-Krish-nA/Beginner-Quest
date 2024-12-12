n=int(input())
def prime(number):
  c=0
  for i in range(2,number):
    if number%i==0:
      c+=1
  if c==0:
    return True
  else:
    return False 
for i in range(n):
  num=int(input())
  for a in range(num):
    for b in range(a+1,num):
      if a+b==num and prime(a) and prime(b):
        print("yes")
        break