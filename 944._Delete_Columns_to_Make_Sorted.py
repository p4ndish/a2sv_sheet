class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        
        for i in range(len(strs[0])):
            ts = ""
            for j in range(len(strs)):
                ts += strs[j][i] 
            if ts != "".join(sorted(ts)):
                res += 1
            # print(ts)
        return res
