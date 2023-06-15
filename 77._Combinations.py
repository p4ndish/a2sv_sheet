class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        
        self.n = n
        def recurse(now, path, k):
            #basecase
            if k == 0:
                res.append(path.copy())
                # print(res)
                return 
            
            for i in range(now, self.n+1):
                path.append(i)
                recurse(i+1, path, k-1)
                
                #if path == k 
                path.pop()
                
        recurse(1,[],k)
        # print(res)
        return res
            
