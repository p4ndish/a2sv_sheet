class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        
        
        
        
        
        
        
        #works but not in order
#         l = 0
#         r = len(nums)-1
        
#         while l <= r:
#             if nums[l] == 0 and nums[r] != 0:
#                 nums[r], nums[l] = nums[l], nums[r]
#                 # self.swap(nums, nums[l],nums[r])
#                 l+=1
#                 r-=1
#             elif nums[r] == 0 and nums[l] != 0:
#                 nums[r], nums[l] = nums[l], nums[r]
#                 # self.swap(nums, num[l],nums[r])
#                 l+=1
#                 r-=1
#             else:
#                 l+=1
            
                
    
    
#     def swap(self, arr, i, j):
