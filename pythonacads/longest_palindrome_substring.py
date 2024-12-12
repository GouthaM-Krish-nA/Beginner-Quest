s=str(input())
def palind(strr):
  return strr==strr[::-1]
d={}
for i in range(len(s)):
  st=s[i]
  for j in range(i+1,len(s)):
    st=st+s[j]
    if palind(st):
      d[st]=len(st)
max_Word =max(d.values())
words=[]
for word,length in d.items():
  if length == max_Word:
    words.append(word)
print(words)
