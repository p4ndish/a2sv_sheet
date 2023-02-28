class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        def isdiagonal(matrix, row, col):
            val = matrix[row][col]
            
            while row < len(matrix) and col < len(matrix[0]):
                if matrix[row][col] != val:
                    return False
                row += 1
                col += 1
            return True
        
        isTrue = True
        r, c = len(matrix), len(matrix[0])
        
        for i in range(r):
            for j in range(c):
                isTrue = isdiagonal(matrix, i, j)
                if isTrue == False:
                    return False
        return isTrue
