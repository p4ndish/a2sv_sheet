class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l < r:
            m = l + (r-l) // 2
            time = sum([math.ceil(i/m) for i in piles])
            if time > h:
                l = m + 1
            else:
                r = m
        return l
