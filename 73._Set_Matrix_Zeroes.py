class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = len(matrix)
        col = len(matrix[0])
        zr, zc = set(), set()
        
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    zr.add(r)
                    zc.add(c)
        # print(zr, zc)
        
        for r in range(row):
            for c in range(col):
                if r in zr or c in zc:
                    matrix[r][c] = 0
        
        
                    
                    
                    
                    
                    
