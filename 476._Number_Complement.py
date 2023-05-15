class Solution:
    def findComplement(self, num: int) -> int:
        # print(dir(bin(8)))
        
        b = bin(num)[2:]
        
        for i in range(len(b)):
            m = 1 << i 
            num ^= m 
        # print(num)
        
        # print(~int(num,2))
        return num 
