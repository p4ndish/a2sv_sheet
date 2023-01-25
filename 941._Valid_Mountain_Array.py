class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        # count the peak of the mount. and count if there are any errors
        hill = 0
        err = 0
        if len(arr) < 3: return False
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                hill += 1
            if arr[i-1] >= arr[i] and arr[i] <= arr[i+1]:
                err += 1
        return hill == 1 and err == 0
        
​
​
