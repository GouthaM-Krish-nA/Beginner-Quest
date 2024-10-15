s=list(map(str,input().split()))
def replce(sl):
    return (sl[0]+(sl[1:len(sl)]).replace(sl[0],'$'))

for i in s:
    print(replce(i))