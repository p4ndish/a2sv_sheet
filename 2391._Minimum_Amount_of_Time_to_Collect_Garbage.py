class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        #find prefix
        pre = [0] + list(accumulate(travel))
        print(pre)
        
        p_prev = 0
        g_prev = 0
        m_prev = 0
        N = len(garbage)
        sums = 0
        for i in range(N):
            for word in garbage[i]:
                pr = pre[i]
                if word == 'P':
                    sums += (pr-p_prev) + 1
                    p_prev = pr
                elif word == 'G':
                    sums += (pr-g_prev) + 1
                    g_prev = pr
                elif word == 'M':
                    sums += (pr-m_prev) + 1
                    m_prev = pr
        # print(sums)
        return sums
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
