class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        aplha = 'abcdefghijklmnopqrstuvwxyz'
        d = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        # print(d)
        # if columnNumber < 27 :
        #     print('no')
        #     return d[columnNumber-1].upper()
        # div, mod = divmod(columnNumber, 26)
        res = ""
        n = columnNumber
        while n > 0:
            # if div > 27:
            #     res += d[div]
            #     break
            # print("in", div, mod, res)
            # n, mod = divmod(n-1, 26)
            # print(/d[(n)%26] )
            res += d[(n-1)%26] 
            n = (n -1) // 26
        # print(res)
        return res[::-1]
            # print("out", n, mod, res)
        # print("->>>", div)
        # if mod :
        #     res += d[mod]
        # if div : res += d[div]
            
        
