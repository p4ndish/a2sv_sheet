class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        
        if not edges:
            return True
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
            
        
            
        def bfs(source, dest):
            visited = set()
            visited.add(source)
            q = deque([source])
            
