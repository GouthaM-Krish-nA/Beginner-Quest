# def frequent_words(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     m=max(d.values())
#     print(d.index(m))
# sts=["i","love","leetcode","i","love"]
# frequent_words(sts)
def k_frequencies(s):
    d={}
    p=[]
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    while d:
        m=max(d.values())
        k=[x for x,y in d.items() if y==m]
        d={f:v for f, v in d.items() if v!=m}
        p.append(k)

    return p
    
s=["i","love","leet","code","i","love","coding","i","like","parn"]
print(k_frequencies(s))
