class Solution:
    def similarPairs(self, words: List[str]) -> int:
        res = 0
        c = defaultdict(int)
        
        for i in words:
            
            s = "".join(sorted(set(i)))
            res += c[s]
            c[s] += 1
        return res
