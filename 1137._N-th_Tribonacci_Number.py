class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        fib    0 1 1 2 3 5 8 13
        trifib 0 1 1 2 4 7 13
        '''
        
        
        def dp(i):
            if i == 0 :
                return i
            if i == 1 or i == 2:
                return 1
            
            if i in memo:
                return memo[i]
            
            r = dp(i-3) + dp(i-2) + dp(i-1)
            memo[i] = r 
            return r 
        
        memo = {}
        return dp(n)
