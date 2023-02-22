class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s=set(nums)
        # print(len(s))
        k = len(s)
        ss = sorted(list(s))
        for i in range(len(ss)):
            val = ss[i]
            nums[i] = val
        return k
        # i = 1
        # j = 1
        # k = len(nums)-1
        # while j <= len(nums)-1:
        #     if nums[j-1] == nums[j]:
        #         j+=1
        #     else:
        #         nums[i] = nums[j]
        #         j+=1
        #         i+=1
        # print(i)
        # print(nums)
        # return i
