class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        N = len(fruits)
        c = {}
        res = 0
        l = 0
        r = 0
        #fruits.sort()
        while r < N:
            if len(c) <= 2:
                c[fruits[r]] = r
                r += 1
            if len(c) > 2:
                min_index = N
                for value in c.values():
                    min_index = min(min_index, value)
                del c[fruits[min_index]]
                l = min_index + 1
            res = max(res, r - l)
        return res
