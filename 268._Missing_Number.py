class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = -1
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1] + 1
