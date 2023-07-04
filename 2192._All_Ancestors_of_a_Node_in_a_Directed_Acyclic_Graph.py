from collections import defaultdict
​
class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        ancestors = defaultdict(set)
        
​
        for from_node, to_node in edges:
            graph[to_node].append(from_node)
        
        def dfs(node, path):
            
            if node in path:
                return
            path.add(node)
            for parent in graph[node]:
                ancestors[node].add(parent)
                ancestors[node].update(ancestors[parent])
                dfs(parent, path)
            path.remove(node)
        
        for node in range(n):    
            dfs(node, set())
        
        # Convert ancestors to sorted lists
        ans = [sorted(list(ancestors[node])) for node in range(n)]
        
        return ans
​
