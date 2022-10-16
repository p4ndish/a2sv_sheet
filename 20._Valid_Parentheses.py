class Solution:
    def isValid(self, s: str) -> bool:
        c = {')':'(',']':'[','}':'{'}
        
        stack = []
        
        for i in s:
            if i in '[{(':
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if c[i] == stack[-1]:
                        stack.pop()
                    else:
                        return False
        print(stack)
        
        return True if not stack else False
