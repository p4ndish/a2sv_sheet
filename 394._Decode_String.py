class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        values = ""
        for i in range(len(s)):
            if s[i] == ']':
                while stack and not stack[-1].isdigit() :
                    p = stack.pop()
                    if p.isalpha():
                        values = p + values
                var = ""
                while stack and stack[-1].isdigit():
                    var =  stack.pop() + var
                stack.append(values * int(var))
                values = ''
            else:
                stack.append(s[i])
        # print(stack)
        return "".join(stack)
        
'''
3[a2[c]]
       ^
strs = "accaccacc"
res = ""
[3, ]
​
2[abc]3[cd]ef
     ^
s = "sdfasd"
[2,[,a,b,c ]
// loop through the stack until we found [
​
'''
