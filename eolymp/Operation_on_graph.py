from collections import defaultdict

n = int(input())
k = int(input())
graph = defaultdict(list)
for i in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 1 :
        mode, n1, n2 = arr
        graph[n1].append(n2)
        graph[n2].append(n1)
    else:
        print(*graph[arr[1]])
