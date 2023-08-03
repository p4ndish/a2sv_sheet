class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def check(i, j):
            return i >= m or j >= n
        # memo = [[0]*n for i in range(m) ]
        # print(memo)
        @cache
        def dp(i,j):
            # if outof bound
            # print(ans)
            if check(i,j):
                return 0
            
            if i == m-1 and j == n-1:
                return 1
            
            # if memo[i][j] :
            #     return memo[i][j]
            # memo[i][j] = ans
            return dp(i+1, j) + dp(i, j+1)
            
        
            
        
        return dp(0, 0)
