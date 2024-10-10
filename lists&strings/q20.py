def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
s=[]
num=int(input("Enter the number:"))
for i in range(2,num):
    if is_prime(i):
        s.append(i)
print(s)
