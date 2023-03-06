class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k 
        res = sum(nums[left:right])/k
        
        cnt_s = sum(nums[left:right])
        # print("orginal: ", cnt_s)
        while right < len(nums):
            cnt_s -= nums[left]
            cnt_s += nums[right]
            # print("curr: ", cnt_s)
            res = max(res, (cnt_s/k))
            
            right += 1 
            left += 1
        return res
