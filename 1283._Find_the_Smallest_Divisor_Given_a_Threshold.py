class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        
        
        def condition(nums, mid):
            ans = 0
            for n in nums:
                ans += ceil(n/mid)
            return ans <= threshold
        
        left , right = 1 , max(nums)
        while left <= right:
            mid = left + (right - left) // 2 
            if condition(nums, mid):
                right = mid - 1
            else:
                left = mid + 1
        print(left, right)
        return left 
        
'''
1,2,3,4,5,6,7,8,9
[1,2,5,9], threshold = 6
l, r = 1, 9
mid = 5
1/5 = 1  + 2/5 = 1 + 5/5 = 1 + 9/5 = 2 == 2
1/3 = 1 + 2/3 = 1 + 5/3 = 2 + 9/3 = 3 == 7
'''
