class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        f = sorted(Counter(nums).items())
        # print(f)
        
        memo = dict()
        def dp(idx):
            if idx >= len(f):
                return 0 
            
            if idx in memo:
                return memo[idx]
            
            if idx < len(f)-1 and f[idx][0]+1 == f[idx+1][0]:
                ch_1 = f[idx][0] * f[idx][1] + dp(idx+2)
            else:
                ch_1 = f[idx][0] * f[idx][1] + dp(idx+1)
                
            ch_2 = dp(idx+1)
            r = max(ch_1 , ch_2)
            memo[idx] = r
            return r
        
        return dp(0)
