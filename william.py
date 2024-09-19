n=int(input())
l=list(map(int, input().split()))
if n<3:
    print('Not enough scores to dtermine the top three.')
l.sort()
l.reverse()

while len(l)>3:
    l.pop(l.index(min(l)))
print(l)