class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if len(piles) == 3:
            return sorted(piles)[-2]
        
        piles.sort()
        N = len(piles)
        c = 0
        for i in range(N-2, (N//3)-1, -2):
            print(piles[i])
            c += piles[i]
            # mn = min(piles[])
        return c
