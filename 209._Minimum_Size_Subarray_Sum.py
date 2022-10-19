class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn = float('inf')
        
        l = 0
        # j = 0
        curr = 0
        print(nums)
        for r in range(len(nums)):
            
            curr+=nums[r]
            while curr >= target:
                mn = min(mn,r- l +1 )
                curr -= nums[l]
                l+=1
        return mn if mn != inf else 0
                
​
​
        
#         count = {0:1}
#         res = float("inf")
#         sums = 0
#         for i in range(len(nums)):
#             sums += nums[i]
#             if sums - target in count :
#                 # print(count, sums-target)
#                 l = 0
#                 tmp = sums
#                 while tmp != target:
#                     tmp -= nums[l]
#                     # nums[l] += 1
#                     l+=1
                
#                 res = min(res, (len(nums)-l))
#                 # count[sums-target] += 1
