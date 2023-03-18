class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
        
                
                p1 = stack.pop()
                p2 = stack.pop()
                s = self.polish(int(p1),int(p2), tokens[i])
                stack.append(s)
            else:
                # print(stack, tokens[i])
                stack.append(int(tokens[i]))
        # print(stack)
        return int(stack[0]) 
    def polish(self, p1, p2, sy):
            if sy == '+':
                return  p2 + p1
            elif sy == '-':
                return p2 - p1
            elif sy == '*':
                return p2 * p1
            else:
                return int(p2 / p1)
