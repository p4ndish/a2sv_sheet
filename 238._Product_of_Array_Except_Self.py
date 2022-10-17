class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
​
        
        
        ans = [1]*len(nums)
        
        l = 1
        for i in range(len(nums)):
            ans[i] = l
            l *= nums[i]
        print(ans)
        r = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= r
            r *= nums[i]
        
        print(ans)
        return ans
   
