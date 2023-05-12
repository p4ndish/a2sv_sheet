class Solution:
    def getSum(self, a: int, b: int) -> int:
       
       
        mx = 0xfff
        c = 0 
        while b & mx > 0:
            c = (a&b) << 1 
            a = a ^ b
            b = c
        if b:
            return a & mx
        else:
            return a
            
            
            
            
            
