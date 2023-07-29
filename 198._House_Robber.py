class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = dict()
        def dp(i):
            
            if i >= len(nums):
                return 0
            
            
            if i in memo:
                return memo[i]
            
            ch_one = nums[i] + dp(i+2)
            ch_two = dp(i+1)
            
            r = max(ch_one, ch_two)
            memo[i] = r 
            return r 
        
        
        return dp(0)
        
        
'''
 0 1 2 3
[1,2,3,1]
​
