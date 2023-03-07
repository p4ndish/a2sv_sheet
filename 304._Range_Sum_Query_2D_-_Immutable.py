class NumMatrix:
​
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [[0] * n for _ in range(m)]
        # print(self.prefix)
        
        for r in range(m):
            for c in range(n):
                top = 0 if r == 0 else self.prefix[r-1][c]
                left = 0 if c == 0 else self.prefix[r][c-1]
                diagonal = 0 if c == 0 or r == 0 else self.prefix[r-1][c-1]
                self.prefix[r][c] = top + left - diagonal + matrix[r][c]
​
​
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefix[row2][col1-1] if col1 > 0 else 0
        top = self.prefix[row1-1][col2] if row1 > 0 else 0
        diagonal = self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0 
        
        return self.prefix[row2][col2] - left - top + diagonal
        
        
        
        
        
​
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
