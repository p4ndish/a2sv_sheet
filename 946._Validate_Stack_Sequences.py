class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p = 0
        is_true = True
        for i in range(len(pushed)):
            # if not is_true: return is_true
            stack.append(pushed[i])
            while stack and stack[-1] == popped[p]:
                stack.pop()
                p+=1
        print(stack,p)
        return True if p == len(popped) else False
        
        
"""
[1,2,3,4,5]
[1,2,]
 [4,3,5,1,2]
j       ^
"""
        
