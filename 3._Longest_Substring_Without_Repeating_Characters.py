class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left , right = 0, 0 
        check = ""
        res = 0
        #c = Counter(s)
        
        N = len(s)
        while right < N:
            if s[right] in check:
                check = s[left:right]
                left += 1
            else:
                check += s[right]
                right += 1
            res = max(res, len(check))
        
        return res
