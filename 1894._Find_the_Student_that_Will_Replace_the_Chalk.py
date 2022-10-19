class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = sum(chalk)
        count = k % sums
        for i in range(len(chalk)):
            if chalk[i] > count:
                return i
            count -= chalk[i]
    
    
'''
 [5,1,5], k = 22
 22- 11 = 11
 11 - 11 = 0
 
 [3,4,1,2], k = 25
 25 % 10 = 5
 3 - 5 .2
 4 > 2
 
'''
