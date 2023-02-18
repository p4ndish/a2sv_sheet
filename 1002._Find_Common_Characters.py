class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # print(set(words[0].union))
        N = len(words) 
        if N == 1:
            return [x for x in words[0]]
        res = list(words[0])
        # print(res)
        for s in words[1:]:
            tmp = []
            print(res)
            for i in s:
                if i in res:
                    tmp.append(i)
                    res.remove(i)
            print(res)
            res = tmp
        return res
    
