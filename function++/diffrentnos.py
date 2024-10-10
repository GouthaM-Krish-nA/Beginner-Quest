#create a fn that takes a sequence of nos and check if the nos are all diffrent from each other
def check_repeat(lst): 
    for i in lst:
        if lst.count(i)>1:
            return False
    return True
l=list(map(int,input().split()))
print(check_repeat(l))