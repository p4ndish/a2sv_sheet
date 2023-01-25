class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = []
        # nums.sort()
        for i in range(len(nums)):
            c = 0
            for j in range(len(nums)):
                if j != i and nums[i] > nums[j]:
                    c += 1
            cnt.append(c)
        return cnt
