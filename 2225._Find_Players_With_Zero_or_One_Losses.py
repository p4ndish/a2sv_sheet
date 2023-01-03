class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        c = defaultdict(int)
        
        
        for winner, losser in matches:
            c[losser] += 1
            if winner not in c:
                c[winner] = 0
        res = [[],[]]
        for key,value in c.items():
            if value == 0:
                res[0].append(key)
            elif value == 1:
                res[1].append(key)
                
                
        # print(res)
        res[0].sort()
        res[1].sort()
        return res
        # print(c)
