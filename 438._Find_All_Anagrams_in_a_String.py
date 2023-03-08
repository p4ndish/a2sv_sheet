class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        left , right = 0, 0 
        cnt_p = Counter(p)
        required_len = len(p)
        
        while right < len(s):
            if s[right] in p:
                cnt_p[s[right]] -= 1 
                
            while (right - left + 1) > required_len : 
                if s[left] in cnt_p:
                    cnt_p[s[left]] += 1 
                left += 1 
                
            if (right -left +1) == required_len and max(cnt_p.values()) == 0:
                res.append(left)
            right += 1 
        return res
