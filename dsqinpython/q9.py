def common_words(words):
    c={}
    for i in words[0]:
        if i in c:
            c[i]+=1
        else:
            c[i]=1
    for i in words[1:]:
        d={}
        for j in i:
            if j in d:
                d[j]+=1
            else:
                d[j]=1
        for i in list(c.keys()):
            if i in d:
                c[i] = min(c[i], d[i])
            else:
                c[i]=0
    result=[]
    for i,j in c.items():
        result.extend([i]*j)
    return result