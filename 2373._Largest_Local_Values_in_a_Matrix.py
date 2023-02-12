class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def getmax(mat, row, col):
            mx = 0
            for r in range(row, row+3):
                for c in range(col,col+3):
                    s = mat[r][c]
                    mx = max(mx, s)
                #     print(mat[r][c] ,end=" | ")
                # print("---")
            return mx
                    
            # pass
        
        row = len(grid)
        col = len(grid[0])
        r = row - 2
        c = col - 2
        
        res = [[0]*c for _ in range(r)]
        r1 , c1 = 0,0
        
        for rows in range(row):
            if rows + 2 >= row:
                break
            for cols in range(col):
                if cols + 2 >= col:break 
                s = getmax(grid, rows, cols)
                # print(s, res[r1][c1], r1, c1, rows)
                res[r1][c1] = s
                c1 += 1
                if c1 == c:
                    c1 = 0
                    r1 += 1
        # print(res)
        return res
