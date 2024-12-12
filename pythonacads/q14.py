#binary seacrh
n=int(input())
num=int(input())
left =1
right=n
while left<=right:
    guess=(left+right)//2
    if guess == num:
        print(f"the number found is {guess}")
        break
    elif num>guess:
        left = guess+1
    else:
        right=guess-1
        

    
