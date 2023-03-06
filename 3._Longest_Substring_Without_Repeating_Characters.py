class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = right = 0 
        # visited = {s[i]: i for i in range(len(s))}
        check = set()
        res = 0
        while right < len(s):
            while right < len(s) and s[right] in check:
                check.remove(s[left])
                left += 1 
                
            check.add(s[right])
            res = max(res, (right-left+1))
            right += 1 
        # print(res)
        return res
        
        
        
        
        
        
        
        
        
        
        
        
