class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        pref = [1] 
        for i in range(len(nums)):
            pref.append(pref[-1]*nums[i])
        suf = [nums[-1]]
        for i in range(len(nums)-2,-1,-1):
            suf.append(suf[-1]*nums[i])
        suf  = suf[::-1] + [1]
        res = []
        for i in range(len(nums)):
            prefix = pref[i]
            suffix = suf[i+1]
            res.append(prefix* suffix)
        # print(res)
        return res
        
'''
[1,2,3,4]
[1,2,6,24]
[24,24,12,4]
'''
