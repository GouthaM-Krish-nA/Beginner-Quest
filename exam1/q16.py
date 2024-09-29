#24BRS1216 goutham
#q18
s=str(input())
word=""
s=s+" "
for i in s:
    if i.isspace():
        c=0
        d=0
        for j in word:
            if j.isdigit():
                c+=1
            if j.isalpha():
                d+=1
            if c>=1 and d>=1 :
                print(word)
            
        word=""
    else:
        word+=i
