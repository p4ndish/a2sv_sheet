class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [] 
        ans = 0 
        arr.append(0)
        n = len(arr)
        m = (10**9) + 7
        for i in range(n):
            # checking if curr is less than the top the stack
            while stack and arr[stack[-1]] >= arr[i]:
                p = stack.pop()
                right_b = i - p 
                if not stack:
                    left_b = p + 1 
                else:
                    left_b = p - stack[-1]
                    
                ans += arr[p] * (left_b * right_b)
            stack.append(i)
            
        return ans % m 
        
        
        
        
        
        
        
        
        
        
        
