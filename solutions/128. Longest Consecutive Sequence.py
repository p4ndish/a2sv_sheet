class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        nums = list(set(nums))
        nums.sort(reverse=True)
        
        res = 0
        stk = [nums[0]]
        
        print(nums)
        for i in range(1, len(nums)):
            
            if stk and abs(nums[i] - stk[-1]) not in [1]:
                # print(nums[i])
                res = max(res, len(stk))
                stk = [nums[i]]
            else:
                
                stk.append(nums[i])
        
        # print(stk)
        return max(res, len(stk))
