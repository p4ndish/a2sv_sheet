class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        [1,2,3,4,5]
        '''
        # if c in [1,0]:
        #     return True
        i = 0
        j = sqrt(c ** 0.5)
        print(j)
        while i <= j :
            f = i ** 2 + j ** 2
            # if f == c: return True
            if f > c:
                j -= 1
            elif f < c:
                i += 1
            else:
                return True
        return False
