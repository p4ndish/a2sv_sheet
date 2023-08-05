class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = defaultdict(int)
        def dp(i):
            if i > n:
                return 0
            if i == n:
                return 1
            if i in memo:
                return memo[i]
            o = dp(i+1) + dp(i+2)
            memo[i] += o 
            return memo[i]
        
        return dp(0)
