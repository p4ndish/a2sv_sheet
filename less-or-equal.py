n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

lo, hi = 1, 10**9
ans = -1
while lo <= hi:
    mid = (lo + hi) // 2
    cnt = sum(1 for x in a if x <= mid)
    if cnt == k:
        ans = mid
        break
    elif cnt < k:
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)
