# s=str(input())
# d={}
# t=str(input())
# st=""
# for i in range(len(s)):
#   st=s[i]
#   for j in range(i+1,len(s)):
#     st=st+s[j]
#     print(st)
#     c=0
#     for k in t:
#       if k in st:
#         c+=1
#     if c==len(t):
#       d[st]=len(st)
# min_Word =min(d.values())
# words=[]
# for word,length in d.items():
#   if length == min_Word:
#     words.append(word)
# print(words)


s=str(input())
real=""
t=str(input())
st=""
for i in range(len(s)):
  st=s[i]
  for j in range(i+1,len(s)):
    st=st+s[j]
    c=0
    for k in t:
      if k in st:
        c+=1
    if c==len(set(t)):
      if len(st)<len(real):
        real=st
print(real)
