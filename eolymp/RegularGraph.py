from collections import defaultdict
n,m = list(map(int, input().split()))
graph = defaultdict(list)


for _ in range(m):
    a, b  = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)


degree = len(graph[1])

for i in range(2, n):
    if len(graph[i]) != degree:
        print("NO")
        exit()
print("YES")
