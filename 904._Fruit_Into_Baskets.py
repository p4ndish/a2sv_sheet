class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # from collections import Counter
        # c = Counter(fruits)
        # if len(c) <= 2:
        #     return sum(c.values())
​
        
        
        d = dict()
        mn = 0
        res = 0
        l = 0
        for r in range(len(fruits)):
            # print(d, fruits[l])
            d[fruits[r]] = r 
            
            if len(d) >= 3:
                mn  = min(d.values())
                del d[fruits[mn]]
                l = mn + 1
            # if len(d) <= 2:
            res = max(res, (r-l + 1))
        
        
        
        return res
        
        
