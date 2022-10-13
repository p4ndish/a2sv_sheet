class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = 0
        res = 0
        c = {0:1}
        
        for i in range(len(nums)):
            sums += nums[i]
            f = sums - k
            if f in c:
                res += c[f] 
            if sums in c:
                c[sums] += 1
            else:
                c[sums] = 1
        return res
