class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [-1] * (len(arr))
        mx = arr[-1]
        
        for i in range(len(arr)-2,-1,-1):
            # if arr[i] < mx:
            res[i] = mx
                
            mx = max(mx, arr[i])
        print(res)
        return res
