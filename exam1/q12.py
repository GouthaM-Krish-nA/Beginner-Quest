n = int(input())
l = list(map(int, input().split()))
p = []
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if (l[i] + l[j] + l[k]) == 0:
                triplet = sorted([l[i], l[j], l[k]])  
                if triplet not in k:  
                    p.append(triplet)

print(p)

              

                
            

