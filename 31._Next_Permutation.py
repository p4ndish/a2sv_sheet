class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n = 0
        N = len(nums)
        for i in range(N-1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i:] = nums[i:][::-1]
                for j in range(i, N):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        break
                n += 1
                break
                
        if not n :
            nums.reverse()
            
        
        
        """
        1,2,3,6,5,4
              ^
              4,5,6
              ^
              1,2,4,3,5,6
        """
        
#         isdec = False
#         isinc = False
        
#         for i in range(len(nums)-1):
#             if nums[i] < nums[i+1]:
#                 isinc = True
#             if nums[i] > nums[i+1]:
#                 isdec = True
        
#         if isinc == True:
