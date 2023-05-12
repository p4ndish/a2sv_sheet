class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        '''
        1   (0 0 0 1)
          ^
        4   (0 1 0 0)
             0 1 0 1
        '''
        
        res = 0 
        m =  x ^ y #using this we find their diference
        while m > 0:
            # this gives use 1 or 0 if m & 1  = 1 the first bits don't match 
            # else it will be 0
            res += m & 1
            # then shifting it by one 
            m >>= 1
        return res
