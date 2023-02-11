class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occ = dict()
        for i in range(len(s)):
            occ[s[i]] = i
        print(occ)
        start, end = 0, 0
        res = []
        
        for i in range(len(s)):
            end = max(end, occ[s[i]])
            # print(res, end)
            if i == end:
                # print("if -> ",i, res, end)
                res.append( end - start +1)
                start = i + 1
                
        return res
​
