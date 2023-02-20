class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # if k == 0:
        #     return 0
        # nums.append(1)
        res = 0
        N = len(nums)
        left = 0
        right = 0
        cpk = 0
        while right < N :
            while left < right and cpk > k:
                if nums[left] == 0:
                    cpk -= 1 
                left += 1 
            
            # if cpk < 0:
            if cpk <= k:
                res = max(res, (right-left))
            if nums[right] == 0:
                cpk += 1
            right += 1
        # print(res)
