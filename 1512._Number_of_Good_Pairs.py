class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         c = defaultdict()
#         res = 0
#         for i in nums:
#             if i in c:
#                 res += 1
#             else:
#                 c[i] = 1
#         return res
        
        
        
