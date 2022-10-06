class Solution:
​
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        r = 0
        res = 0
        v = 0
        vowel = 'aeiou'
        # print(s[l:k])
        for r in range(len(s)):
            # cur = s[l:r+1]
            if s[r] in vowel:
                v+=1
            if (r-l + 1) == k:
                res = max(res, v)
                if s[l] in vowel:
                    v -=1
                l+=1
        return res
