class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, end, arr):
            res.append(arr[:])
            for i in range(start, end):
                arr.append(nums[i])
                backtrack(i+1, end, arr)
                arr.pop()
                
        res = []
        N = len(nums)
        
        backtrack(0, N, [])
        return res
