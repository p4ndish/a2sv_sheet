# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
K = int(input())

arr = list(input().split())

cnt = Counter(arr)
# print(cnt)

res = float("inf")
val = 0
for i in cnt:
    # print(i)
    if cnt[i] < res:
        val = i
        res = cnt[i]
print(val)


'''
1 2 3 6 5
4 4 2 5 3 
6 1 6 5 3 
2 4 1 2 5 
1 4 3 6 8 
4 3 1 5 6 2 
(1,5) (2,5) (3,5) (4,5) (5,5) (6,5) (8,1)
'''
