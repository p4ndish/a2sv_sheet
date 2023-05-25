class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        '''
        question: given the rotten and fresh oranges in a grid find the 
        minimum path that rottens all the fresh oranges
        
        solution: since bfs is best at finding shortest path we use bfs and 
                  given the grid we store the rotten oranges x,y cordinate in the
                  qeue so that we can check for every up,down,right,left grid 
                  cells as negibhours and if there is fresh in the 4 directions we
                  can rotten them  in a minute and add them to the qeue because 
                  their might be a fresh neighbhour for that direction and then
                  continue with the other element in our qeue
                  
        '''
        r, c = len(grid), len(grid[0])
        q = deque()
        
        res = 0 
        fresh = 0 
        # add the rotten
        for row in range(r):
            for col in range(c):
                if grid[row][col] == 2 :
                    q.append([row,col])
                elif grid[row][col] == 1:
                    fresh += 1 
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
​
        
        
        while q and fresh > 0:
            res += 1 
            for _ in range(len(q)):
                px, py = q.popleft()
​
                for x, y in dirs:
