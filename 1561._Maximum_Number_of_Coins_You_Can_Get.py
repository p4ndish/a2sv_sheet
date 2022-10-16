class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        '''
        choose the first index then the last two indexs so on....
        or sort them and calculate how many times i can choose a num from alice -1 index
        '''
        piles.sort()
        l = len(piles)
        i = 0 
        j = 2
        k = l//3
        res = 0 
        while i < k:
            res += piles[l-j]
            i+=1
            j+=2
        return res
        
