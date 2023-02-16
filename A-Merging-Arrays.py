n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

N = len(arr1)
n = len(arr2)
l = 0
r = 0 
res = []
while l < N and r < n :
    if arr1[l] < arr2[r]:
        res.append(arr1[l])
        l += 1 
    elif arr1[l] > arr2[r]:
        res.append(arr2[r])
        r += 1 
    else:
        res.append(arr1[l])
        res.append(arr2[r])
        l += 1 
        r += 1 

if l < N : res.extend(arr1[l:])
if r < n : res.extend(arr2[r:])
print(*res)
