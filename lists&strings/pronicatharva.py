n=int(input())

for i in range(1,n+1):
    if i*(i+1)==n:
        print(i)
        print(i+1) 
        break
else:
    print("This number is not Pronic.")
        
