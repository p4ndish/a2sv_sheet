class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        question: given a matrix that contains 0,1 1 represents island and 0 water, find the largest
        area of the island 
        
        solution: since we need a visit all the matrix cordinate up,down,left,right and if there is
        any an island go to that island and do this repeatdly 
        '''
        
        
        
        
        
        
        
        
        directions = [
            (-1,0), (1,0), (0,-1), (0,1)
        ]
        
        
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0]) 
        
        self.tmp = 0
        def dfs(r, c):
            visited[r][c] = True
            
            t = 1
            for dr, dy in directions:
                newR, newC = dr + r, dy + c
                
                if inbound(newR, newC) and not visited[newR][newC] and grid[newR][newC] == 1:
                    self.tmp += 1
                    t += dfs(newR, newC)
