class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        ans = [0]* N
        stack = deque()
        
        for i,val in enumerate(temperatures):
            
            while stack and stack[-1][0] < val:
                pval,pi = stack.pop()
                ans[pi] = (i - pi)
                
            
            stack.append([val,i])
        # print(ans)
        return ans
        
'''
[73,74,75,71,69,72,76,73]
                      ^
[(75,2)  (76,6)] (73,0) (74,1)
ans = [1,1,4,2,1,1,0,0]
'''
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
