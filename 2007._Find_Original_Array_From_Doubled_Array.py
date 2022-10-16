class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0 :
            return []
        
        c = Counter(changed)
        changed.sort()
        res = []
        for i in range(len(changed)):
            t = changed[i]
            if c[t] == 0:
                continue
            elif c[t*2] > 0 :
                res.append(t)
                c[t]-=1
                c[t*2] -= 1
            else:
                return []
            
        print(res)
        return res
"""
[1,3,4,2,6,8]
[1,2,3,4,6,8]
       *
"""
