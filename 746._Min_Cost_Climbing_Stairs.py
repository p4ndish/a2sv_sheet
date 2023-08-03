class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        memo = defaultdict(int)
        @cache
        def dp(i):
            if i >= len(cost):
                return 0 
            
            # if i in memo:
            #     return memo[i]
            
            ch2 = dp(i+1)
            ch1 = dp(i+2)
            
            r = min(ch1, ch2) + cost[i]
            # memo[i] = r 
            
            return r 
            # pass
            
        
        
