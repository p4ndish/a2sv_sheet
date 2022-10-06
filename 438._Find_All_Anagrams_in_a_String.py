class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = 0
        res = []
        c = Counter(p)
        clen = len(p)
        N = len(s)
        for r in range(N):
            if s[r] in c:
                c[s[r]] -= 1
            
                    
            if (r - l + 1) > clen:
                while (r - l + 1) > clen and l <= r:
                    if s[l] in c:
                        c[s[l]] += 1
                    l += 1
            
            if max(c.values()) == 0  and (r - l + 1) == clen:
                res.append(l)
        return res
    
'''
size = 3
res = [0,]
size = 2
a = 1,0 b = 1,0
abab
  ^
 ^
'''
