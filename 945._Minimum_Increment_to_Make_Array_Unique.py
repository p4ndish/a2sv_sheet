class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort()
        mx, ans = nums[0],0
        # [ 1,2,2 ]
        for i in nums:
            ans+= max(0, mx-i)
            mx = max(mx+1,i+1)
        return ans
#         mx = 0
#         res = 0
#         visited = set()
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i] in visited:
#                 f = (mx - nums[i]) + 1
#                 res+=f
#                 nums[i] +=f
#             mx = max(mx, nums[i])
#             visited.add(nums[i])
​
#         return res
            
        
'''    2 1
[3,2,1,2,5,7]
       ^
         4-1 = 4
       3-2 = 1
mx = 4
c = 4 + 2
vist = (3,2,1,4,5,7)
​
'''
