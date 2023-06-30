class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        
        
        for a, b in richer:
            graph[b].append(a)
            
            
        def dfs(node):
            if ans[node] >= 0:
                return ans[node]
            ans[node] = node
            for neighbour in graph[node]:
                if quiet[ans[node]] > quiet[dfs(neighbour)]:
                    ans[node] = ans[neighbour] 
            return ans[node]
        
        ans = [-1] * len(quiet)
        for i in range(len(quiet)):
            a = dfs(i)
            # ans.append(a)
        
        return ans
