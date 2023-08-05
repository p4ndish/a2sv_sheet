class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = defaultdict(int)
        self.cnt = 0
        # @cache
        def dp(i, sum_):
            # r = 0
            if i == len(nums) and sum_ == target:
                return 1
            if i == len(nums):
                return 0
            
            # if sum_ == target:
            #     return 1 
            if (i,sum_) in memo :
                return memo[(i,sum_)]
            p = dp(i+1, nums[i] + sum_) + dp(i+1, sum_ - nums[i] )
            memo[(i, sum_)] = p 
            # memo[]
            return memo[(i,sum_)]
            
            # print(r)
            # return r 
        return dp(0,0)
