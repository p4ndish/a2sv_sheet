class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and i < j:
                    res += 1
        return res
​
#         from itertools import combinations
#         s= combinations(nums,2)
#         # print(s)
#         count = 0
#         for i in list(s):
#             # print(i[0])
#             if i[0] == i[1]:
#                 count += 1
#             # print(i)
#         return count
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
