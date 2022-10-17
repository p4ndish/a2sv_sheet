class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        right = the sum of the( nums) - the curr idx - previous sum'ed idx values(starts with 0)  
        left = previous index sum with the current index
        
        '''
        #manuall prefix sum
        # sums = [0]*len(nums)
        # sums[0] = nums[0]
        # for i in range(1,len(nums)):
        #     sums[i] = sums[i-1] + nums[i]
        # print(sums)
        l = 0
        for i in range(len(nums)):
            right = sum(nums) - l - nums[i]
            if l == right:
                return i
            else:
                l+=nums[i]
        
