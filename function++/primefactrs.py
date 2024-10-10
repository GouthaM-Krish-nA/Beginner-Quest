def is_prime(num):
    for i in range(2,int(num**0.5)+1):
        if num %i==0:
            return False
    return True
def prime_factors(n):
    i=2
    s=[]
    while(n//i)!=1:
        if n%i==0:
            s.append(i)
            n=n//i
        else:
            i+=1
    s.append(n)
    return s
p=int(input())
print(prime_factors(p))

    