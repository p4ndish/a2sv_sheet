n, m = list(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

N = len(arr1)
n = len(arr2)
l = N - 1 
r = n -1 
res = [0] * n 
k = n - 1 
while r >= 0 and l >= 0:
    while arr1[l] >= arr2[r] and l >=0:
        l -= 1
    
    res[k] = l + 1 
    k -= 1
    # l -= 1 
    r -= 1 
print(*res)
    
