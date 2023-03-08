class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = right = 0 
        mnl = float(inf)
        
        sums = 0
        while right < len(nums):
            sums += nums[right]
            while sums >= target and left < right:
                mnl = min(mnl, (right-left+1))
                sums -= nums[left]
                left += 1 
            if sums >= target:
                mnl = min(mnl, (right-left+1))
            right += 1 
            
        # print(mnl)
        return mnl if mnl != inf else 0 
