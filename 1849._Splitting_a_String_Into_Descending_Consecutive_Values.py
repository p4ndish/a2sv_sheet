class Solution:
    def splitString(self, s: str) -> bool:
        
        
        N = len(s)
        def dfs(index, prev):
            if index == N:
                return True
            
            for j in range(index, N):
                val = int(s[index:j+1])
                if val+1 == prev and dfs(j+1, val):
                    return True
            return False
        
        
        for i in range(N-1):
            val = int(s[:i+1])
            if dfs(i+1, val):
                return True
        return False
