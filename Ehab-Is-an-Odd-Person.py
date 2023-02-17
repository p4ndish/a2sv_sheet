n  = int(input())
arr = list(map(int, input().split()))

O, E = 0,0
for i in arr:
    if i % 2:
        O += 1
    else:
        E += 1

if O and E :
    arr.sort()
print(*arr)
