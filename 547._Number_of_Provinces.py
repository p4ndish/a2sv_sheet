class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj_list = defaultdict(list)
        visited = [False] * (n + 1)  
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj_list[i+1].append(j+1)  
​
        def dfs(node):
            visited[node] = True
            for neighbor in adj_list[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
​
        count = 0
        for i in range(1, n+1):
            if not visited[i]:
                count += 1
                dfs(i)
​
        return count
​
