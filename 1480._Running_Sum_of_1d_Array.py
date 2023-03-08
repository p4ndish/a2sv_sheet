class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pref = [nums[0]]
        for n in nums[1:]:
            pref.append((n+pref[-1]))
        return pref
