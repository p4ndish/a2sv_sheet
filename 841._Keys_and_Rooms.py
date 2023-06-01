class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        
        def dfs(node):
            if node not in visited:
                visited.add(node)
                for r in rooms[node]:
                    dfs(r)
        
        dfs(0)
        return len(visited) == len(rooms)
