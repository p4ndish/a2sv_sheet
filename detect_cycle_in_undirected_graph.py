from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		
		def dfs(adj,node, visited, parent):
            visited.add(node)

            for N in adj[node]:
                if N not in visited:
                    if dfs(adj, N, visited, node):
                        return True
                elif N != parent :
                    return True
            return False
         
        
        visited = set()
        for i in range(V):
            if i not in visited:
                if dfs(adj, i, visited, -1):
                    return True
        return False
		
