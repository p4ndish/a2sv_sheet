class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for i in tokens:
            if i in "+-*/":
                x = stack.pop()
                y = stack.pop()
                ans = self.verify(i,int(y),int(x))
                stack.append(ans)
            else:
                stack.append(int(i))
        return stack[0]
        # print(stack)
    def verify(self, opr, y, x):
        # print(x,y)
        if opr == '+':
            return y + x
        elif opr == '-':
            return y - x
        elif opr == '*':
            return y * x
        else:
            return int(y/x)
