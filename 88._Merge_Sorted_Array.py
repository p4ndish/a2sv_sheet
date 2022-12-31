class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # if not m < n : return nums2
        # if not n < m : return nums1
        place = (m + n) - 1
        l = m -1
        r = n - 1
        
        while r >= 0:
            if nums2[r] > nums1[l]:
                #placing it starting from the end
                nums1[place] = nums2[r]
                r -= 1
                place -= 1
                l -= 1
                print(nums1)
            else:
                nums1[place] = nums1[l]
                nums1[l] = nums2[r]
                place -= 1
                # l -= 1
                r -= 1
        
        # print(nums1)
                
        # brute-forcing...
