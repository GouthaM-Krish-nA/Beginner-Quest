hr=int(input())
min=int(input())
bill=0
if hr>7 :
  print("Invalid Input")
else:
  if hr>=5:
    bill=bill+200
    hr=hr-5
bill=bill+hr*50
print("the bil amount is :Rs",bill+min)



