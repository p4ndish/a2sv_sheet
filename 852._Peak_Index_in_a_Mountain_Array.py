class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        res = arr[0]
        resi = 0
        for i in range(1, len(arr)-1):
            if arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                res = max(res, arr[i])
                resi = i
        return resi
        
        
        return 0 
