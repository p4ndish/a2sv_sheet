class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * (N)
        l,r = 0,(N-1)
        for i in range(N-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        # print(nums)
        for i in range(N):
            if nums[i] != 0:
                # c += 1
                res[l] = nums[i]
                l += 1
        # print(res)
            # nums[i], nums[j] = nums[j], nums[i]
        return res
