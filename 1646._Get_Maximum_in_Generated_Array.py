class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n < 2:
            return n
        a = [0] * (n+1) 
        a[0] = 0 
        a[1] = 1 
        ans = 1 
        for i in range(2, n+1):
            if i % 2 == 1:
                a[i] = a[i//2] + a[i//2+1]
            else:
                a[i] = a[i//2]
            ans = max(ans, a[i])
            
        return ans
