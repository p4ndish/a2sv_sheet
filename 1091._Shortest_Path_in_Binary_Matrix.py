class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
​
        
        
        
        
        
        directions = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (1, -1), (1, 1), (-1, 1)
        ]
        def inbound(row,col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
​
        # print(visited)
        n = len(grid)
        
        def bfs(x, y):
            visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
            # count = -1
            q = deque()
            q.append((x,y,1))
            # cnt = 0 
            while q :
                
                for _ in range(len(q)):
