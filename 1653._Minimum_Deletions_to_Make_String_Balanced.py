class Solution:
    def minimumDeletions(self, s: str) -> int:
        cnt = 0 
        res = 0 
        
        
        for i in range(len(s)-1, -1,-1):
            if s[i] == 'a':
                cnt += 1
            if s[i] == 'b' and cnt:
                cnt -= 1 
                res += 1
        return res
