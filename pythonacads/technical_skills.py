n=int(input())
for i in range(n):
  if i%3==0 and i%5==0 :
    print("SneakPeak")
  elif i%3==0 and i%5!=0 :
    print("Sneak")
  elif i%3!=0 and i%5==0 :
    print("Peak")
  else:
    print(i)