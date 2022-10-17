class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        # print(c.items())
        # res = []
        # for i in sorted(c.items(), key=lambda x: (-x[1],x[0])):
        #     res.append(i[0])
        # return res[0:k]
        return nsmallest(k, c.keys(), key=lambda x:(-c[x],x))
