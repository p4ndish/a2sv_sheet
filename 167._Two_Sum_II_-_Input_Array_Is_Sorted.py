class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        N = len(numbers)
        left = 0
        right = N -1
        while left <= right:
            n  = numbers[left] + numbers[right]
            if n == target:
                return [left+1, right+1]
            if n > target: right -= 1
            else: left += 1
        
