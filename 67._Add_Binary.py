class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''
        0011
        0001
        '''
        
        carry = 0
        res = ""
        
        a = list(a)
        b = list(b)
        
        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())
            # print(carry)
            res += str(carry % 2)
            carry //= 2
            
        return res[::-1]
