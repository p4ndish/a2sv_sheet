class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr_op = "+"
        curr_num = ""
        s += " "
        for i in range(len(s)):
            if s[i].isdigit():
                curr_num += s[i]
            if s[i] in "+/*-" or i == len(s)-1:
                print(i,s[i])
                n = int(curr_num)
                if curr_op == "*":
                    stack[-1] = stack[-1] * n
                elif curr_op == "/":
                    stack[-1] = int(stack[-1] / n)
                    
                elif curr_op == "+":
                    stack.append(n)
                elif curr_op == "-":
                    stack.append(n*-1)
                curr_num = ""
                curr_op = s[i]
        return sum(stack)
"""
" 3+5 / 2-1"
op = '+'
["",3,+,5,"",/,"",2,-,1]
[3,2,-1]
"""
