class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) <= 1:
            return "0"
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and num[i] < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        print(stack)
        
        # if k :
        #     return "0"
        res = "".join(stack)
        res = res.lstrip('0')
        if k:
            res = res[:-k]
        return res if res else "0"
        # return res.lstrip('0') if len(res) > 1 else "0"
        
        
        
        
        
        
        
'''
"1432219", k = 3
      ^
1 4
1 2 1 9 
k = 0
​
 "10200", k = 1
      ^
 0 2 0 0 
 k = 0
 
'''
