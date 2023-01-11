class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                ans.append(nums[nums[j]])
            break
        # print(ans)
        return ans
