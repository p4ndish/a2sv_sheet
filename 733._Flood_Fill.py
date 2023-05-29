class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.color = color
        directions = [
            (-1,0),(1,0),(0,-1),(0,1)
        ]
        visited = [ [0 for j in range(len(image[0]))]for i in range(len(image)) ]
        # print(visited)
        
        def inbound(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        old_color = image[sr][sc]
        def dfs(sr, sc, visited):
            visited[sr][sc] = True
            if image[sr][sc] == old_color:
                image[sr][sc] = color
                for dr, dc in directions:
                    new_row = sr + dr
                    new_col = sc + dc
                    if inbound(new_row, new_col) and not visited[new_row][new_col]:
                        dfs(new_row, new_col, visited)
                        
        dfs(sr, sc, visited)
        # print(image)
        return image
            
        
        
        
