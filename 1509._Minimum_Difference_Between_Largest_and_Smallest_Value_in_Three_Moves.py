class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 4 :
            return 0 
        
        a = nums[-4] - nums[0]
        b = nums[-3] - nums[1]
        c = nums[-2] - nums[2]
        d = nums[-1] - nums[3]
        return min(a, b, c, d)
        s = set(nums)
​
        
'''
1,5,0,10,14
0 1 | 5 10 14
​
6,6,0,1,1,4,6
0 1 1 4 | 6 6 6
​
'''
        
        
