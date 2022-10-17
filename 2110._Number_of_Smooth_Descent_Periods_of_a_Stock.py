class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        N =  len(prices)
        res = 1
        l = 0
        r = 1
        c = 1
        while r < N:
            if prices[r-1] == prices[r]+1 :
                c += 1
            else:
                c = 1
                l = r
                # l += 1
            res += c
            r += 1
        print(res)
        return res
​
        # res = 1
        # cont = 1
        # for i in range(1, len(prices)):
        #     if prices[i-1] - prices[i] == 1:
        #         cont += 1
        #     else:
        #         cont = 1
        #     res += (cont)
        # print(res)
        
        # print(res)
     
            
