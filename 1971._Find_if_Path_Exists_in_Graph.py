class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def find(node):
            if node == parent[node]:
                return node
            
            return find(parent[node])
        
        def union(node1, node2):
            par1, par2 = find(node1), find(node2)
            if par1 != par2:
                parent[par1] = parent[par2]
        
        parent = [i for i in range(n)]
                
                
        for x, y in edges:
            union(x, y)
                      
        return find(source) == find(destination)
                
