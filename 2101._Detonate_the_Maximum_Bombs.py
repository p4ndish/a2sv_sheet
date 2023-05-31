class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    distance = sqrt(pow(bombs[j][0] - bombs[i][0], 2) +pow(bombs[j][1] - bombs[i][1], 2))
                    # print(distance, bombs[i], bombs[j])
                    if distance <= bombs[i][2]:
                        graph[i].append(j)
                    
        
        def dfs(node, visited):
            if visited[node]:
                return 0 
            visited[node] = True
            count = 1
            for edge in graph[node]:
                if not visited[edge]:
                    count += dfs(edge, visited)
            return count
        
        max_ = 0
        for i in range(len(bombs)):
