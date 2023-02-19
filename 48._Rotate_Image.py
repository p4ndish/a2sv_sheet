class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        (0,0)(0,3)
        (0,1)(1,3)
        (0,2)(2,3)
        
        
        """
        def formula(r,c,colLen):
            return c ,colLen - 1 - r
        m = len(matrix[0])
        l = 0
        r = m - 1 
        while l < r:
            for i in range(r-l):
                top, bottom = l, r 
                
                topleft = matrix[top][l+i]
                matrix[top][l+i] = matrix[bottom - i][l]
                matrix[bottom-i][l] = matrix[bottom][r-i]
                matrix[bottom][r-i] = matrix[top + i][r] #top + i
                matrix[top + i][r] = topleft
            l += 1 
            r -= 1
            
