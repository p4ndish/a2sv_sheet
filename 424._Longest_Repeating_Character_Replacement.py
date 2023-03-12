class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0 
        res = 0 
        c = defaultdict(int)
        cnt_max = 0
        
        
        while right < len(s):
            c[s[right]] += 1 
            cnt_max = max(cnt_max, c[s[right]])
            if (right-left+1) - cnt_max > k :
                c[s[left]] -= 1 
                left += 1 
            res = max(res, right-left+1)
            right += 1 
            
        return res
