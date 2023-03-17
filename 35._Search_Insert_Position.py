class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] < target:
                left = mid + 1
                # print(left, right)
            elif nums[mid] > target :
                right = mid -1 
                # print(left, right)
            else:
                return mid 
        return right +1
