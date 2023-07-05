class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        degree =defaultdict(int)
        
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
        
        to_dfs = -1
        for key, val in degree.items():
            if val == 1:
                to_dfs = key
                break
                
                
        def dfs(node, visited, ans):
            if node in visited:
                return 
            visited.add(node)
            for N in graph[node]:
                if N not in visited:
                    ans.append(N)
                    # self.arr.append(N)
                    dfs(N, visited, ans)
                    
        # self.arr = [to_dfs]
        visited = set()
        ans = [to_dfs]
        dfs(to_dfs, visited, ans)
        # print(ans)
        return ans
