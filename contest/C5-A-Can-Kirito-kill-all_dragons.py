s, n = map(int, input().split())
 
tmp = []
for i in range(n):
    
    drs,bon = map(int, input().split())
    tmp.append((drs,bon))
    
    
tmp.sort(key=lambda x: (x[0], -x[1]))
 
for dragon, bonus in tmp:
    if s > dragon:
        s += bonus
    else:
        print("NO")
        exit()
print("YES")
