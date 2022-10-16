class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        s = list(s)
        tmp = []
        for i in range(len(s)):
            # print(stack)
            if s[i] == ')':
                while stack[-1] != '(':
                    if stack[-1] == '(': break
                    tmp.append(stack.pop())
                stack[-1] = ""
                stack.extend(tmp)
                tmp = []
                s[i] = ""
                
            
            stack.append(s[i])
        return "".join(stack)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = []
