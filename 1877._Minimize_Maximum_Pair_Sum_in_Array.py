class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        n = len(nums)-1
        res = 0
        while i < len(nums)//2:
            res = max(res,(nums[i]+nums[n]))
            # print(nums[i],nums[n])
            i+=1 
            n-=1
        return res
