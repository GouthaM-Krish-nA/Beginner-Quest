def anagrams(st):
    c={}
    for i in st:
        b= "".join(sorted(i))
        if b in c:
           c[b].append(i)
        else:
            c[b]=[i]
    return c
st=["ate","eat","pun" ,"nup"]    
print(anagrams(st))