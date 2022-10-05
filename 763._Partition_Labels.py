class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        c = {v:i for i,v in enumerate(s)}
        # print(c)
        size = 0
        end = 0
        res = []
        for i in range(len(s)):
            if c[s[i]] > end:
                end = c[s[i]]
            size += 1
            if i == end:
                res.append(size)
                size = 0
        return res
                
    
    
    
    
    
"""
012345678 9
ababcbaca d e f e g d e h i j h k l i j
​
