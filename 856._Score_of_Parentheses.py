class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        # res = 0 
        
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                p = stack.pop()
                stack[-1] += max(p * 2, 1)
                
        return stack[-1]
        
'''
"()"
"(())()()()()()((()))"
"()()"
'''
