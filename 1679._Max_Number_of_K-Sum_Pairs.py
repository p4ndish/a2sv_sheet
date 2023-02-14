class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        N = len(nums)
        l = 0
        r = N - 1 
        res = 0
        while l < r:
            x = nums[l] + nums[r]
            if x > k :
                r -= 1
            elif x < k:
                l += 1
            else:
                res += 1
                l += 1
                r -= 1
        print(res)
        return res
        # d = defaultdict(int)
        # res = 0
        # s = ""
        # for i in range(len(nums)):
        #     x = k - nums[i]
            
        #     if x in d and d[x] > 0 and str(i) not in  s:
        #         s += str(i)
        #         # print(x, d)
        #         d[x] -= 1
        #         if d[x] <= 0: del d[x]
        #         res += 1
        #     if str(i) not in  s:
        #         d[nums[i]] += 1
