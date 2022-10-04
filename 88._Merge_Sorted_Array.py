class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        ptrone  = m - 1
        ptrtwo  = n - 1
        idx = m + n -1
        
        while ptrtwo >= 0:
            if ptrone >= 0 and nums1[ptrone] > nums2[ptrtwo]:
                nums1[idx] = nums1[ptrone]
                ptrone -=1
            else:
                nums1[idx] = nums2[ptrtwo]
                ptrtwo -=1
            idx -= 1
        
#         if not nums1 or not nums2:
#             return 
#         N = len(nums1)
#         ptr1 = 0
#         ptr2 = 0
        
#         ptr3 = 0
#         for i in range(N):
#             if nums1[i] == 0:
#                 ptr3 = i
#                 break 
                
        
#         print(ptr3)
#         for i in range(len(nums2)):
#             tar = nums2[i]
#             while nums1[ptr1] <= tar and nums1[ptr1] != 0:
